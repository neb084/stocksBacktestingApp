import functions as f
import constants as c


class Stocks:  # Used to store stock data and preform necessary functions
    def __init__(self, symbol):
        """
        Requires a Stock Symbol to create. Initializes historical & analytical data lists. \n
        NOTES: Declares symbol in string format. Required input in uppercase
        """
        self.symbol = symbol.upper()

        # Initializes the historical_data list, leaving all fields blank. candles keyword creates a blank list for
        # inputting the historical data: datetime, open, close, high, & low. The candles list, requires additional
        # initialization
        self.historical_data = [{'historical_name': '', 'start_datetime': '', 'end_datetime': '', 'period_type': '',
                                 'period': '', 'frequency_type': '', 'frequency': '', 'extended_hours': '',
                                 'candles': []}]

        # Initializes the analytical_data list, leaving all fields blank. The additional keywords & lists required to
        # create the analytical data requires additional creation/initialization. This is done so that the function
        # can be modified to specific back tests
        self.analytical_data = [{'analysis_name': '', 'historical_name_link': '', 'buy_signal': '', 'sell_signal': '',
                                 'analysis_type': '', 'data': []}]

    # Initializing methods
    def initialize_new_historical_data(self):
        """
        Initializes the historical_data list, leaving all fields blank. candles keyword creates a blank list for
        inputting the historical data: datetime, open, close, high, & low. The candles list, requires additional
        initialization. \n
        NOTE: Returns the index of the appended list (the new historical_data list)\n
        :return: Returns the index of the appended list (the new historical_data list)
        :rtype: Integer
        """
        # Initializes the historical_data list, leaving all fields blank. candles keyword creates a blank list for
        # inputting the historical data: datetime, open, close, high, & low. The candles list, requires additional
        # initialization
        self.historical_data.append({'historical_name': '', 'start_datetime': '', 'end_datetime': '', 'period_type': '',
                                     'period': '', 'frequency_type': '', 'frequency': '', 'extended_hours': '',
                                     'candles': []})
        return len(self.historical_data) - 1  # Returns the index of the appended list

    def initialize_new_analytical_data(self):
        """
        Initializes the analytical_data list, leaving all fields blank. The additional keywords & lists required to
        create the analytical data requires additional creation/initialization. This is done so that the function
        can be modified to specific back tests  \n
        NOTE: Returns the index of the appended list (the new analytical_data list)     \n
        :return: Returns the index of the appended list (the new analytical_data list)
        :rtype: Integer
        """
        self.analytical_data = [{'analysis_name': '', 'historical_name_link': '', 'buy_signal': '', 'sell_signal': '',
                                 'analysis_type': ''}]
        return len(self.analytical_data) - 1  # Returns the index of the appended list

    # historical_data getters & setters
    def set_historical_name_hd(self, list_index_hd, historical_name):
        """
        Sets the historical name for historical_data. \n
        Historical name is used to define the data pull from the API and also links the analytical_data
        to the historical_data
        """
        self.historical_data[list_index_hd]['historical_name'] = historical_name

    def get_historical_name_hd(self, list_index_hd):
        """Returns historical_name for historical_data"""
        return self.historical_data[list_index_hd]['historical_name']

    def set_start_datetime_hd(self, list_index_hd, start_datetime):
        """
        Sets the start_datetime for historical_data in ms. \n
        NOTE: The datetime stamp for minute is exact, however when accessing the API, it is set backwards 2 hours
        for daily, weekly, & monthly. For example, in historical_data, a date entry would be stored as
        "9/28/20 00:00". But in the TD API, it would be listed as "9/27/20 22:00". Noting that it is actually stored
        in milliseconds as a int/long, versus a formatted string
        """
        self.historical_data[list_index_hd]['start_datetime'] = start_datetime

    def get_start_datetime_hd(self, list_index_hd):
        """
        Returns the start_datetime for historical_data in ms \n
        NOTE: The datetime stamp for minute is exact, however when accessing the API, it is set backwards 2 hours
        for daily, weekly, & monthly. For example, in historical_data, a date entry would be stored as
        "9/28/20 00:00". But in the TD API, it would be listed as "9/27/20 22:00". Noting that it is actually stored
        in milliseconds as a int/long, versus a formatted string
        """
        return self.historical_data[list_index_hd].start_datetime

    def set_end_datetime_hd(self, list_index_hd, end_datetime):
        """
        Sets the end_datetime for historical_data in ms \n
        NOTE: The datetime stamp for minute is exact, however when accessing the API, it is set backwards 2 hours
        for daily, weekly, & monthly. For example, in historical_data, a date entry would be stored as
        "9/28/20 00:00". But in the TD API, it would be listed as "9/27/20 22:00". Noting that it is actually stored
        in milliseconds as a int/long, versus a formatted string
        """
        self.historical_data[list_index_hd]['end_datetime'] = end_datetime

    def get_end_datetime_hd(self, list_index_hd):
        """
        Returns the end_datetime for historical_data in ms \n
        NOTE: The datetime stamp for minute is exact, however when accessing the API, it is set backwards 2 hours
        for daily, weekly, & monthly. For example, in historical_data, a date entry would be stored as
        "9/28/20 00:00". But in the TD API, it would be listed as "9/27/20 22:00". Noting that it is actually stored
        in milliseconds as a int/long, versus a formatted string
        """
        return self.historical_data[list_index_hd].end_datetime

    def set_period_type_hd(self, list_index_hd, period_type):
        """
        Set period_type \n
        NOTE: period_types are: 'day', 'month', 'year', or 'ytd' \n
        NOTE: if frequency type is 'minute', use 'day'... \n
        NOTE: if frequency type is 'day', 'week' or 'month', use 'year'
        """
        self.historical_data[list_index_hd]['period_type'] = period_type

    def get_period_type_hd(self, list_index_hd):  # Get period_type
        """
        NOTE: period_types are: 'day', 'month', 'year', or 'ytd' \n
        NOTE: if frequency type is 'minute', use 'day'... \n
        NOTE: if frequency type is 'day', 'week' or 'month', use 'year' \n
        """
        return self.historical_data[list_index_hd]['period_type']

    def set_period_hd(self, list_index_hd, period):
        """
        Set period \n
        NOTE: if using specific end & starts dates, then period should be left blank as ''
        """
        self.historical_data[list_index_hd]['period'] = period

    def get_period_hd(self, list_index_hd):
        """
        Get period \n
        NOTE: if using specific end & starts dates, then period should be left blank as ''
        """
        return self.historical_data[list_index_hd]['period']

    def set_frequency_type_hd(self, list_index_hd, frequency_type):
        """
        Set frequency_type \n
        Valid frequencyTypes by periodType (defaults marked with an asterisk): \n
        day: ‘minute’* \n
        month: ‘daily’, ‘weekly’* \n
        year: ‘daily’, ‘weekly’, ‘monthly’* \n
        ytd: ‘daily’, ‘weekly’*
        """
        self.historical_data[list_index_hd]['frequency_type'] = frequency_type

    def get_frequency_type_hd(self, list_index_hd):
        """
        Get frequency_type \n
        Valid frequencyTypes by periodType (defaults marked with an asterisk): \n
        day: ‘minute’* \n
        month: ‘daily’, ‘weekly’* \n
        year: ‘daily’, ‘weekly’, ‘monthly’* \n
        ytd: ‘daily’, ‘weekly’*
        """
        return self.historical_data[list_index_hd]['frequency_type']
    
    def set_frequency_hd(self, list_index_hd, frequency):
        """
        Set frequency \n
        Valid frequencies by frequencyType (defaults marked with an asterisk): \n
        minute: 1*, 5, 10, 15, 30 \n
        daily: 1* \n
        weekly: 1* \n
        monthly: 1* \n
        """
        self.historical_data[list_index_hd]['frequency'] = frequency

    def get_frequency_hd(self, list_index_hd):
        """
        Get frequency \n
        Valid frequencies by frequencyType (defaults marked with an asterisk): \n
        minute: 1*, 5, 10, 15, 30 \n
        daily: 1* \n
        weekly: 1* \n
        monthly: 1* \n
        """
        return self.historical_data[list_index_hd]['frequency']

    def set_extended_hours_hd(self, list_index_hd, extended_hours):
        """
        Sets extended hours to determine if data is desired. 'true' = included extended hours;
        'false' = do not include extended hours \n
        NOTE: To stay consistent with TD API, the boolean values are stored as a string and all letters MUST be
        lowercase, like 'false' or 'true' versus actual boolean literal
        """
        self.historical_data[list_index_hd]['extended_hours'] = extended_hours

    def is_extended_hours_hd(self, list_index_hd):
        """
        Gets extended hours boolean. 'true' = included extended hours; 'false' = do not include extended hours \n
        NOTE: To stay consistent with TD API, the boolean values are stored as a string and all letters MUST be
        lowercase, like 'false' or 'true' versus actual boolean literal
        """
        return self.historical_data[list_index_hd]['extended_hours']

    def set_candles_hd(self, list_index_hd, candles_list):
        """
        Loops through list sent as argument and stores values \n
        :param list_index_hd: 0-n (used to specific historical data pull)
        :type list_index_hd: Integer
        :param candles_list: {'open': Float, 'close': Float, 'high': Float, 'low': Float, 'volume': Integer/Long}
        :type candles_list: List
        """

        if self.get_frequency_type_hd(list_index_hd) == 'minute':  # minute frequency doesn't require a timestamp adjustment
            for i in range(len(candles_list)):
                self.historical_data[list_index_hd]['candles'].append({
                    'datetime': candles_list[i]['datetime'], 'open': candles_list[i]['open'],
                    'close': candles_list[i]['close'], 'high': candles_list[i]['high'], 'low': candles_list[i]['low'],
                    'volume': candles_list[i]['volume']})
        else:  # daily, weekly & monthly frequencies require a 2 hour added adjustment to match
            for i in range(len(candles_list)):
                self.historical_data[list_index_hd]['candles'].append({
                    'datetime': (candles_list[i]['datetime'] + c.MILLISECONDS_PER_HOUR * 2), 'open': candles_list[i]['open'],
                    'close': candles_list[i]['close'], 'high': candles_list[i]['high'], 'low': candles_list[i]['low'],
                    'volume': candles_list[i]['volume']})

    def get_values_from_candles_key_hd(self, list_index_hd, key):
        list_to_return = []  # initialize list_to_return
        for i in range(len(self.historical_data[list_index_hd]['candles'])):  # loop through candles list to break out
            list_to_return.append(self.historical_data[list_index_hd]['candles'][i][key])
        return list_to_return

    # analytical_data getters & setters
    def set_analytical_name_ad(self, list_index, analytical_name):
        """
        Sets the analytical_name for analytical_data. \n
        analytical_name is used to define the data pull from the API and also links the analytical_data
        to the analytical_data.
        \n
        :param list_index: 0-n
        :type list_index: Integer
        :param analytical_name: Defines the name of the test being done
        :type analytical_name: String
        """
        self.analytical_data[list_index]['analytical_name'] = analytical_name

    def get_analytical_name_ad(self, list_index):
        """
        Returns analytical_name for analytical_data. analytical_name is used to define the data pull from the API
        and also links the analytical_data to the analytical_data. \n
        :param list_index: 0-n
        :type list_index: Integer
        :return: Name of analysis being done
        :rtype: String
        """
        return self.analytical_data[list_index]['analytical_name']

    def set_historical_name_link_ad(self, list_index, historical_name_link_ad):
        """
        Sets the historical_name_link used to sync up with historical_data. \n
        :param list_index: 0-n
        :type list_index: Integer
        :param historical_name_link_ad: Name of historical data pull
        :type historical_name_link_ad: String
        """
        self.analytical_data[list_index]['historical_name_link_ad'] = historical_name_link_ad

    def get_historical_name_link_ad(self, list_index):
        """
        Gets the historical_name_link used to sync up with historical_data. \n
        :param list_index: 0-n
        :type list_index: Integer
        :return: Name of historical data pull
        :rtype: String
        """
        return self.analytical_data[list_index]['historical_name_link_ad']
    
    def set_buy_execution_ad(self, list_index, buy_execution):
        """
        Use the coded constants... i.e. BUY_OPEN_CURRENT_DAY, BUY_CLOSE_CURRENT_DAY, BUY_OPEN_NEXT_DAY, 
        BUY_CLOSE_NEXT_DAY\n
        :param list_index: 0-n
        :type list_index: Integer
        :param buy_execution: 
        :type buy_execution: String
        """
        self.analytical_data[list_index]['buy_execution'] = buy_execution

    def get_buy_execution_ad(self, list_index):
        """
        Use the coded constants when comparing... i.e. BUY_OPEN_CURRENT_DAY, BUY_CLOSE_CURRENT_DAY, BUY_OPEN_NEXT_DAY, 
        BUY_CLOSE_NEXT_DAY\n
        :param list_index: 0-n
        :type list_index: Integer
        :return: Returns a string for BUY signals.
        :rtype: String 
        """
        return self.analytical_data[list_index]['buy_execution']

    def set_sell_execution_ad(self, list_index, sell_execution):
        """
        Use the coded constants... i.e. SELL_OPEN_CURRENT_DAY, SELL_CLOSE_CURRENT_DAY, SELL_OPEN_NEXT_DAY, 
        SELL_CLOSE_NEXT_DAY\n
        :param list_index: 0-n
        :type list_index: Integer
        :param sell_execution: 
        :type sell_execution: String
        """
        self.analytical_data[list_index]['sell_execution'] = sell_execution

    def get_sell_execution_ad(self, list_index):
        """
        Use the coded constants when comparing... i.e. SELL_OPEN_CURRENT_DAY, SELL_CLOSE_CURRENT_DAY, SELL_OPEN_NEXT_DAY, 
        SELL_CLOSE_NEXT_DAY\n
        :param list_index: 0-n
        :type list_index: Integer
        :return: Returns a string for SELL signals.
        :rtype: String 
        """
        return self.analytical_data[list_index]['sell_execution']

    def set_analysis_type_ad(self, list_index, analysis_type):
        """
        Use coded constants to set, like: ANALYSIS_2MA \n
        :param list_index: 0-n
        :type list_index: Integer
        :param analysis_type: Coded string used to define the analysis_type
        :type analysis_type: String
        """
        self.analytical_data[list_index]['analysis_type'] = analysis_type
        
    def get_analysis_type_ad(self, list_index):
        """
        Use coded constants to compare, like: ANALYSIS_2MA \n
        :param list_index: 0-n
        :type list_index: Integer
        :return: Coded string used to define the analysis_type
        :rtype: String
        """
        return self.analytical_data[list_index]['analysis_type']
    
    # 2 Moving Averages functions (coded constant = ANALYSIS_MA2) getters & setters
    def set_ma2_value_to_use_from_candle_ad(self, list_index_ad, ma2_value_to_use):
        """
        Define whether you are using the CLOSE (normally), OPEN, HIGH, or LOW using coded constant \n
        :param list_index_ad: 0-n
        :type list_index_ad: Integer
        :param ma2_value_to_use: Coded constant like: CLOSE, OPEN, HIGH or LOW
        :type ma2_value_to_use: String
        """
        self.analytical_data[list_index_ad]['ma2_value_to_use'] = ma2_value_to_use

    def get_ma2_value_to_use_from_candle_ad(self, list_index_ad):
        """
        Gets coded constant you are using, like: CLOSE (normally), OPEN, HIGH, or LOW using coded constant \n
        Always compare against a coded constant \n
        :param list_index_ad: 0-n
        :type list_index_ad: Integer
        :param ma2_value_to_use: Coded constant like: CLOSE, OPEN, HIGH or LOW
        :type ma2_value_to_use: String
        """
        return self.analytical_data[list_index_ad]['ma2_value_to_use']

    def set_ma2_type_short_ad(self, list_index_ad, ma2_type_short):
        """
        Sets the Moving Average type for the Short MA. Use coded constants \n
        :param list_index_ad: 0-n
        :type list_index_ad: Integer
        :param ma2_type_short: Use coded constant like SMA or EMA
        :type ma2_type_short: String
        """
        self.analytical_data[list_index_ad]['ma2_type_short'] = ma2_type_short

    def get_ma2_type_short_ad(self, list_index_ad):
        """
        Gets the Moving Average type for the Short MA. Use coded constants when comparing it like SMA or EMA \n
        :param list_index_ad: 0-n
        :type list_index_ad: Integer
        :return: Returns a coded string
        :rtype: String
        """
        return self.analytical_data[list_index_ad]['ma2_type_short']
    
    def set_ma2_length_short_ad(self, list_index_ad, ma2_length_short):
        """
        Sets the Moving Average length for the Short MA \n
        :param list_index_ad: 0-n
        :type list_index_ad: Integer
        :param ma2_length_short: Value must be >=2
        :type ma2_length_short: Integer
        """
        self.analytical_data[list_index_ad]['ma2_length_short'] = ma2_length_short

    def get_ma2_length_short_ad(self, list_index_ad):
        """
        Gets the Moving Average length for the Short MA \n
        :param list_index_ad: 0-n
        :type list_index_ad: Integer
        :return: Returns an integer representing the length of the Short MA
        :rtype: Integer
        """
        return self.analytical_data[list_index_ad]['ma2_length_short']
    
    def set_ma2_type_long_ad(self, list_index_ad, ma2_type_long):
        """
        Sets the Moving Average type for the Long MA. Use coded constants \n
        :param list_index_ad: 0-n
        :type list_index_ad: Integer
        :param ma2_type_long: Use coded constant like SMA or EMA
        :type ma2_type_long: String
        """
        self.analytical_data[list_index_ad]['ma2_type_long'] = ma2_type_long

    def get_ma2_type_long_ad(self, list_index_ad):
        """
        Gets the Moving Average type for the Long MA. Use coded constants when comparing it like SMA or EMA \n
        :param list_index_ad: 0-n
        :type list_index_ad: Integer
        :return: Returns a coded string
        :rtype: String
        """
        return self.analytical_data[list_index_ad]['ma2_type_long']
    
    def set_ma2_length_long_ad(self, list_index_ad, ma2_length_long):
        """
        Sets the Moving Average length for the Short MA \n
        :param list_index_ad: 0-n
        :type list_index_ad: Integer
        :param ma2_length_long: Value must be >=3 & must be >ma_length_short
        :type ma2_length_long: Integer
        """
        self.analytical_data[list_index_ad]['ma2_length_long'] = ma2_length_long

    def get_ma2_length_long_ad(self, list_index_ad):
        """
        Gets the Moving Average length for the Long MA \n
        :param list_index_ad: 0-n
        :type list_index_ad: Integer
        :return: Returns an integer representing the length of the Long MA
        :rtype: Integer
        """
        return self.analytical_data[list_index_ad]['ma2_length_long']

    def set_ma2_data_ad(self, list_index_ad):
        
        # Find the historical data's index to get the candles
        list_index_hd = 0
        for list_index_hd in range(len(self.historical_data)):
            if self.get_historical_name_link_ad(list_index_ad) == self.get_historical_name_hd(list_index_hd):
                break  # exit loop and stores the index in the list_index_hd for later use

        # Get the specific value from the candles to be included in the MA and make a list to send for MA's
        list_for_ma = []
        if self.get_ma2_value_to_use_from_candle_ad(list_index_ad) == c.CLOSE:
            list_for_ma = self.get_values_from_candles_key_hd(list_index_hd, 'close')
        elif self.get_ma2_value_to_use_from_candle_ad(list_index_ad) == c.OPEN:
            list_for_ma = self.get_values_from_candles_key_hd(list_index_hd, 'open')
        elif self.get_ma2_value_to_use_from_candle_ad(list_index_ad) == c.HIGH:
            list_for_ma = self.get_values_from_candles_key_hd(list_index_hd, 'high')
        elif self.get_ma2_value_to_use_from_candle_ad(list_index_ad) == c.LOW:
            list_for_ma = self.get_values_from_candles_key_hd(list_index_hd, 'low')
        else:
            print("Invalid argument")
            exit(1)

        # Determine Short MA type and send to return to function
        short_values_list = []
        if self.get_ma2_type_short_ad(list_index_ad) == c.SMA:
            short_values_list = f.sma(self.get_ma2_length_short_ad(list_index_ad), list_for_ma)

        elif self.get_ma2_type_short_ad(list_index_ad) == c.EMA:
            print('PLACE HOLDER')
            """
            Place holder !!!!!!
            """

        # Determine Long MA type and send to return to function
        long_values_list = []
        if self.get_ma2_type_long_ad(list_index_ad) == c.SMA:
            long_values_list = f.sma(self.get_ma2_length_long_ad(list_index_ad), list_for_ma)
        elif self.get_ma2_type_long_ad(list_index_ad) == c.EMA:
            print('PLACE HOLDER')
            """
            Place holder !!!!!!
            """

        # calculate over_under values
        over_under_list = []
        for i in range(len(short_values_list)):
            if long_values_list[i] == 0 or short_values_list[i] == 0:
                over_under_list.append(c.NA)
            elif short_values_list[i] > long_values_list[i]:
                over_under_list.append(c.OVER)
            elif short_values_list[i] < long_values_list[i]:
                over_under_list.append(c.UNDER)
            elif short_values_list[i] == long_values_list[i]:
                over_under_list.append(c.EQUALS)
            else:
                print("ERROR!")
                exit(1)

        # calculate buy/sell signal based upon criteria listed
        signal_list = []
        signal_price_list = []
        buy_signal_created = False
        skip = False
        for i in range(len(over_under_list)):
            if skip: # used for some criteria purposes
                skip = False
                continue
            elif i == 0:  # if it is the first signal, always N/A
                signal_list.append(c.NA)
                signal_price_list.append(c.NA)
            elif over_under_list[i] == over_under_list[i-1] or over_under_list[i] == c.EQUALS or over_under_list[i-1] == c.NA:  #if over_under is the same as the prior or both current ma's are equal
                signal_list.append(c.NA)
                signal_price_list.append(c.NA)
            elif over_under_list[i] == c.OVER:
                buy_signal_created = True  # this can be repeated. It used to avoid a sell signal being created before the first buy signal
                # determine which buy order is created and get the value
                if self.get_buy_execution_ad(list_index_ad) == c.BUY_CLOSE_CURRENT_DAY:
                    signal_list.append(c.BUY)
                    signal_price_list.append(self.historical_data[list_index_hd]['candles'][i]['close'])
                elif self.get_buy_execution_ad(list_index_ad) == c.BUY_OPEN_CURRENT_DAY:
                    signal_list.append(c.BUY)
                    signal_price_list.append(self.historical_data[list_index_hd]['candles'][i]['open'])
                elif self.get_buy_execution_ad(list_index_ad) == c.BUY_CLOSE_NEXT_DAY:
                    if i+1 != len(over_under_list): #as long as the next item is not the end of the list
                        signal_list.append(c.NA) #N/A for current day
                        signal_list.append(c.BUY) # Buy for next day
                        signal_price_list.append(self.historical_data[list_index_hd]['candles'][i+1]['close'])
                        skip = True  # tell loop to skip 1 day, because it was already determined
                elif self.get_buy_execution_ad(list_index_ad) == c.BUY_OPEN_NEXT_DAY:
                    if i+1 != len(over_under_list): #as long as the next item is not the end of the list
                        signal_list.append(c.NA) #N/A for current day
                        signal_list.append(c.BUY) # Buy for next day
                        signal_price_list.append(self.historical_data[list_index_hd]['candles'][i+1]['open'])
                        skip = True  # tell loop to skip 1 day, because it was already determined
                else:
                    print("Error!!!")
            elif over_under_list[i] == c.UNDER and buy_signal_created:  # if sell signal is created after the first buy signal is created
                # determine which sell order is created and get the value
                if self.get_sell_execution_ad(list_index_ad) == c.SELL_CLOSE_CURRENT_DAY:
                    signal_list.append(c.SELL)
                    signal_price_list.append(self.historical_data[list_index_hd]['candles'][i]['close'])
                elif self.get_sell_execution_ad(list_index_ad) == c.SELL_OPEN_CURRENT_DAY:
                    signal_list.append(c.SELL)
                    signal_price_list.append(self.historical_data[list_index_hd]['candles'][i]['open'])
                elif self.get_sell_execution_ad(list_index_ad) == c.SELL_CLOSE_NEXT_DAY:
                    if i+1 != len(over_under_list):  # as long as the next item is not the end of the list
                        signal_list.append(c.NA)  # N/A for current day
                        signal_list.append(c.SELL)  # Buy for next day
                        signal_price_list.append(self.historical_data[list_index_hd]['candles'][i+1]['close'])
                        skip = True  # tell loop to skip 1 day, because it was already determined
                elif self.get_sell_execution_ad(list_index_ad) == c.SELL_OPEN_NEXT_DAY:
                    if i+1 != len(over_under_list):  # as long as the next item is not the end of the list
                        signal_list.append(c.NA)  # N/A for current day
                        signal_list.append(c.BUY)  # Buy for next day
                        signal_price_list.append(self.historical_data[list_index_hd]['candles'][i+1]['open'])
                        skip = True  # tell loop to skip 1 day, because it was already determined
            else:
                signal_list.append(c.NA)

        # Loop to set the data
        for i in range(len(short_values_list)):
            self.analytical_data[list_index_ad]['data']\
                .append({'short_value': short_values_list[i], 'long_value': long_values_list[i],
                         'over_under': over_under_list[i]})
            if signal_list[i] == c.BUY or signal_list[i] == c.SELL:  # check if buy/sell signal and set if so set
                self.analytical_data[list_index_ad]['data'][i]\
                    .update({'buy_sell_order': signal_list[i], 'buy_sell_price': signal_price_list[i]})



