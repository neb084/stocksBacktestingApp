# This class file is to hold all the basic functions needed for the Backtesting App
import datetime as dt
import constants as c

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


