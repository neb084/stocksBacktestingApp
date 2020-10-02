# This class file is to hold all the basic functions needed for the Backtesting App
import datetime as dt
import constants as c
import requests

# All date & time related functions
# NOTES: timestamps are designated for the start of each candle
#        timestamps for daily/weekly/month are set back (-2) hours to local time
#        timestamps for minute candles of any frequency (1, 5, 10, 15, & 30 min) are not offset


def get_timestamp_current_local_to_send_to_api():
    return round(dt.datetime.timestamp(dt.datetime.now()) * c.MILLISECONDS_PER_SECOND)


def convert_dwm_timestamps_from_api(timestamp_dwm): #only for daily, weekly & monthly candles
    # Timestamps for the daily/weekly/monthly candles need to have 2 hours added
    # to them to be formatted properly as the right day at 00:00 time
    # this doesn't apply to minute candles of any frequency (1, 5, 10, 15, & 30 min)
    return timestamp_dwm + c.MILLISECONDS_PER_HOUR * 2


def format_timestamp_datetime(timestamp):  # formatted like: 2020-09-24 06:30:00
    return dt.datetime.fromtimestamp(timestamp // c.MILLISECONDS_PER_SECOND)


def format_date_dddmmmddyyyy(timestamp):  # formatted like: Thu, Sep 24 2020
    return dt.date.fromtimestamp(timestamp // c.MILLISECONDS_PER_SECOND).strftime('%a, %b %d %Y')


def format_date_mmddyyyy(timestamp):  # formatted like: 09/24/2020
    return dt.date.fromtimestamp(timestamp // c.MILLISECONDS_PER_SECOND).strftime('%m/%d/%Y')


def format_date_mmddyy(timestamp):  # formatted like: 09/24/20
    return dt.date.fromtimestamp(timestamp // c.MILLISECONDS_PER_SECOND).strftime('%m/%d/%y')


def format_time_hhmm_ampm(timestamp):  # formatted like: 06:30 AM
    return dt.datetime.fromtimestamp(timestamp // c.MILLISECONDS_PER_SECOND).strftime('%I:%M %p')


# All stock analysis functions
def get_over_under_short_long(short_value, long_value):  # Returns OVER, UNDER, EQUALS or N/A when comparing short & long MA's
    if long_value == 0 or short_value == 0:  # N/A is used for when there is no data yet
        return c.NA
    elif short_value > long_value:
        return c.OVER
    elif short_value < long_value:
        return c.UNDER
    elif short_value == long_value:
        return c.EQUALS


def sma(length, values_for_sma): # return list with SMA values based upon

    """
    Return list with SMA values based upon length and value submitted (usually the CLOSE of the candle, but can be OPEN, HIGH, LOW or VOLUME)
    :param length:  Lookback length for the SMA. Must be >=2
    :type length: Integer
    :param values_for_sma: List of Float/Integer values being coverted into SMA data. Usually the CLOSES of the candle,
    but can send value desired.
    :type values_for_sma: List of Floats/Integer
    :return: Return list with SMA values based upon length and value submitted (usually the CLOSE of the candle)
    :rtype: List of Floats/Integers
    """
    sma_list = []  # initialize sma list

    # add 0 to the list for the first areas where SMA can't be calculated
    for i in range(length-1):
        sma_list.append(0)

    # calculate SMA and store in list
    for i in range(length-1, len(values_for_sma)):
        sma_sum = 0  # for calculating SMA
        for j in range(i-(length-1), i+1):
            sma_sum = sma_sum + values_for_sma[j]
        sma_list.append(sma_sum / length)

    return sma_list


# API functions

"""
NEED TO HAVE A CALL TO THIS FUNCTION!!! with parameters
"""
def get_price_history_from_API(**kwargs):
    # Method/function to call to website and upload parameters and return results
    # **kwargs means it can handle many arguments that are defined by a keyword in which the method can handle

    key = 'HGDUKYGX3ZYVKTSJZTEEVEPUANXS2AU0'

    # URL address for API, pulling 'symbol' key from kwargs
    url = 'https://api.tdameritrade.com/v1/marketdata/{}/pricehistory'.format(kwargs.get('symbol'))

    # Initialize dictionary
    user_params = {}
    # Add 'apikey' to "user_params" dictionary
    user_params.update({'apikey': key})

    # for every argument ("arg") in kwargs, add it to the "user_params" dictionary
    for arg in kwargs:
        user_params.update({arg: kwargs.get(arg)})

    # Return the results by sending "url" and the supplied "params" (params is a keyword on the API),
    # json is the format it is being received in
    data_from_API = requests.get(url, params=user_params).json()  # get dictionary from API
    return data_from_API['candles']  # return only the candles