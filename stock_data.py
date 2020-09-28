import functions


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
                                 'analysis_type': ''}]

    # historical_data getters & setters
    def set_historical_name_hd(self, list_index, historical_name):
        """
        Sets the historical name for historical_data. \n
        Historical name is used to define the data pull from the API and also links the analytical_data
        to the historical_data
        """
        self.historical_data[list_index]['historical_name'] = historical_name

    def get_historical_name_hd(self, list_index):
        """Returns historical_name for historical_data"""
        return self.historical_data[list_index]['historical_name']

    def set_start_datetime_hd(self, list_index, start_datetime):
        """
        Sets the start_datetime for historical_data in ms. \n
        NOTE: The datetime stamp for minute is exact, however when accessing the API, it is set backwards 2 hours
        for daily, weekly, & monthly. For example, in historical_data, a date entry would be stored as
        "9/28/20 00:00". But in the TD API, it would be listed as "9/27/20 22:00". Noting that it is actually stored
        in milliseconds as a int/long, versus a formatted string
        """
        self.historical_data[list_index]['start_datetime'] = start_datetime

    def get_start_datetime_hd(self, list_index):
        """
        Returns the start_datetime for historical_data in ms \n
        NOTE: The datetime stamp for minute is exact, however when accessing the API, it is set backwards 2 hours
        for daily, weekly, & monthly. For example, in historical_data, a date entry would be stored as
        "9/28/20 00:00". But in the TD API, it would be listed as "9/27/20 22:00". Noting that it is actually stored
        in milliseconds as a int/long, versus a formatted string
        """
        return self.historical_data[list_index].start_datetime

    def set_end_datetime_hd(self, list_index, end_datetime):
        """
        Sets the end_datetime for historical_data in ms \n
        NOTE: The datetime stamp for minute is exact, however when accessing the API, it is set backwards 2 hours
        for daily, weekly, & monthly. For example, in historical_data, a date entry would be stored as
        "9/28/20 00:00". But in the TD API, it would be listed as "9/27/20 22:00". Noting that it is actually stored
        in milliseconds as a int/long, versus a formatted string
        """
        self.historical_data[list_index]['end_datetime'] = end_datetime

    def get_end_datetime_hd(self, list_index):
        """
        Returns the end_datetime for historical_data in ms \n
        NOTE: The datetime stamp for minute is exact, however when accessing the API, it is set backwards 2 hours
        for daily, weekly, & monthly. For example, in historical_data, a date entry would be stored as
        "9/28/20 00:00". But in the TD API, it would be listed as "9/27/20 22:00". Noting that it is actually stored
        in milliseconds as a int/long, versus a formatted string
        """
        return self.historical_data[list_index].end_datetime

    def set_period_type_hd(self, list_index, period_type):
        """
        Set period_type \n
        NOTE: period_types are: 'day', 'month', 'year', or 'ytd' \n
        NOTE: if frequency type is 'minute', use 'day'... \n
        NOTE: if frequency type is 'day', 'week' or 'month', use 'year'
        """
        self.historical_data[list_index]['period_type'] = period_type

    def get_period_type_hd(self, list_index):  # Get period_type
        """
        NOTE: period_types are: 'day', 'month', 'year', or 'ytd' \n
        NOTE: if frequency type is 'minute', use 'day'... \n
        NOTE: if frequency type is 'day', 'week' or 'month', use 'year' \n
        """
        return self.historical_data[list_index]['period_type']

    def set_period_hd(self, list_index, period):
        """
        Set period \n
        NOTE: if using specific end & starts dates, then period should be left blank as ''
        """
        self.historical_data[list_index]['period'] = period

    def get_period_hd(self, list_index):
        """
        Get period \n
        NOTE: if using specific end & starts dates, then period should be left blank as ''
        """
        return self.historical_data[list_index]['period']

    def set_frequency_type_hd(self, list_index, frequency_type):
        """
        Set frequency_type \n
        Valid frequencyTypes by periodType (defaults marked with an asterisk): \n
        day: ‘minute’* \n
        month: ‘daily’, ‘weekly’* \n
        year: ‘daily’, ‘weekly’, ‘monthly’* \n
        ytd: ‘daily’, ‘weekly’*
        """
        self.historical_data[list_index]['frequency_type'] = frequency_type

    def get_frequency_type_hd(self, list_index):
        """
        Get frequency_type \n
        Valid frequencyTypes by periodType (defaults marked with an asterisk): \n
        day: ‘minute’* \n
        month: ‘daily’, ‘weekly’* \n
        year: ‘daily’, ‘weekly’, ‘monthly’* \n
        ytd: ‘daily’, ‘weekly’*
        """
        return self.historical_data[list_index]['frequency_type']
    
    def set_frequency_hd(self, list_index, frequency):
        """
        Set frequency \n
        Valid frequencies by frequencyType (defaults marked with an asterisk): \n
        minute: 1*, 5, 10, 15, 30 \n
        daily: 1* \n
        weekly: 1* \n
        monthly: 1* \n
        """
        self.historical_data[list_index]['frequency'] = frequency

    def get_frequency_hd(self, list_index):
        """
        Get frequency \n
        Valid frequencies by frequencyType (defaults marked with an asterisk): \n
        minute: 1*, 5, 10, 15, 30 \n
        daily: 1* \n
        weekly: 1* \n
        monthly: 1* \n
        """
        return self.historical_data[list_index]['frequency']

    def set_extended_hours_hd(self, list_index, extended_hours):
        """
        Sets extended hours to determine if data is desired. 'true' = included extended hours;
        'false' = do not include extended hours \n
        NOTE: To stay consistent with TD API, the boolean values are stored as a string and all letters MUST be
        lowercase, like 'false' or 'true' versus actual boolean literal
        """
        self.historical_data[list_index]['extended_hours'] = extended_hours

    def is_extended_hours_hd(self, list_index):
        """
        Gets extended hours boolean. 'true' = included extended hours; 'false' = do not include extended hours \n
        NOTE: To stay consistent with TD API, the boolean values are stored as a string and all letters MUST be
        lowercase, like 'false' or 'true' versus actual boolean literal
        """
        return self.historical_data[list_index]['extended_hours']

    def set_candles_hd(self, list_index, candles_list):
        """
        Loops through list sent as argument and stores values \n
        :param list_index: 0-n (used to specific historical data pull)
        :type list_index: Integer
        :param candles_list: {'open': Float, 'close': Float, 'high': Float, 'low': Float, 'volume': Integer/Long}
        :type candles_list: List
        """
        for i in range(len(candles_list)):
            self.historical_data[list_index]['candles'].append({
                'datetime': candles_list[i]['datetime'], 'open': candles_list[i]['open'],
                'close': candles_list[i]['close'], 'high': candles_list[i]['high'], 'low': candles_list[i]['low'],
                'volume': candles_list[i]['volume']})

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

    def set_historical_name_link_ad(self, list_index, historical_name_link):
        """
        Sets the historical_name_link used to sync up with historical_data. \n
        :param list_index: 0-n
        :type list_index: Integer
        :param historical_name_link: Name of historical data pull
        :type historical_name_link: String
        """
        self.analytical_data[list_index]['historical_name_link'] = historical_name_link

    def get_historical_name_link_ad(self, list_index):
        """
        Gets the historical_name_link used to sync up with historical_data. \n
        :param list_index: 0-n
        :type list_index: Integer
        :return: Name of historical data pull
        :rtype: String
        """
        return self.analytical_data[list_index]['historical_name_link_ad']
    
    def set_buy_execution(self, list_index, buy_execution):
        """
        Use the coded constants... i.e. BUY_OPEN_CURRENT_DAY, BUY_CLOSE_CURRENT_DAY, BUY_OPEN_NEXT_DAY, 
        BUY_CLOSE_NEXT_DAY\n
        :param list_index: 0-n
        :type list_index: Integer
        :param buy_execution: 
        :type buy_execution: String
        """
        self.analytical_data[list_index]['buy_execution'] = buy_execution

    def get_buy_execution(self, list_index):
        """
        Use the coded constants when comparing... i.e. BUY_OPEN_CURRENT_DAY, BUY_CLOSE_CURRENT_DAY, BUY_OPEN_NEXT_DAY, 
        BUY_CLOSE_NEXT_DAY\n
        :param list_index: 0-n
        :type list_index: Integer
        :return: Returns a string for BUY signals.
        :rtype: String 
        """
        return self.analytical_data[list_index]['buy_execution']

    def set_sell_execution(self, list_index, sell_execution):
        """
        Use the coded constants... i.e. SELL_OPEN_CURRENT_DAY, SELL_CLOSE_CURRENT_DAY, SELL_OPEN_NEXT_DAY, 
        SELL_CLOSE_NEXT_DAY\n
        :param list_index: 0-n
        :type list_index: Integer
        :param sell_execution: 
        :type sell_execution: String
        """
        self.analytical_data[list_index]['sell_execution'] = sell_execution

    def get_sell_execution(self, list_index):
        """
        Use the coded constants when comparing... i.e. SELL_OPEN_CURRENT_DAY, SELL_CLOSE_CURRENT_DAY, SELL_OPEN_NEXT_DAY, 
        SELL_CLOSE_NEXT_DAY\n
        :param list_index: 0-n
        :type list_index: Integer
        :return: Returns a string for SELL signals.
        :rtype: String 
        """
        return self.analytical_data[list_index]['sell_execution']

    def set_analysis_type(self, list_index, analysis_type):
        """
        Use coded constants to set, like: ANALYSIS_2MA \n
        :param list_index: 0-n
        :type list_index: Integer
        :param analysis_type: Coded string used to define the analysis_type
        :type analysis_type: String
        """
        self.analytical_data[list_index]['analysis_type'] = analysis_type
        
    def set_analysis_type(self, list_index):
        """
        Use coded constants to compare, like: ANALYSIS_2MA \n
        :param list_index: 0-n
        :type list_index: Integer
        :return: Coded string used to define the analysis_type
        :rtype: String
        """
        return self.analytical_data[list_index]['analysis_type']
    
    # 2 Moving Averages functions, getters & setters
