import constants as c
import functions as f

import datetime
import stock_data

stocks = stock_data.Stocks("AAPL")
stocks.set_period_type_hd(0, "year")
stocks.set_frequency_type_hd(0, "daily")
stocks.set_frequency_hd(0, 1)
stocks.set_extended_hours_hd(0, "false")
stocks.set_historical_name_hd(0, "test1")
stocks.set_candles_hd(0, f.get_price_history_from_API(symbol=stocks.symbol, period=stocks.get_period_hd(0),  periodType=stocks.get_period_type_hd(0), frequency=stocks.get_frequency_hd(0), frequencyType=stocks.get_frequency_type_hd(0), needExtendedHoursData=stocks.is_extended_hours_hd(0)))
stocks.set_analytical_name_ad(0, "ad1")
stocks.set_historical_name_link_ad(0, stocks.get_historical_name_hd(0))
stocks.set_buy_execution_ad(0, c.BUY_OPEN_NEXT_DAY)
stocks.set_sell_execution_ad(0, c.SELL_OPEN_NEXT_DAY)
stocks.set_analysis_type_ad(0, c.ANALYSIS_MA2)
stocks.set_ma2_value_to_use_from_candle_ad(0, c.CLOSE)
stocks.set_ma2_type_short_ad(0, c.SMA)
stocks.set_ma2_length_short_ad(0, 9)
stocks.set_ma2_type_long_ad(0, c.SMA)
stocks.set_ma2_length_long_ad(0, 20)
stocks.set_ma2_data_ad(0)



for i in range(len(stocks.historical_data[0]['candles'])):
    print("Date:", f.format_date_dddmmmddyyyy(stocks.historical_data[0]['candles'][i]['datetime']),
          f"= Close:{round(stocks.historical_data[0]['candles'][i]['close'], 2):>7.2f}",
          f"Short:{round(stocks.analytical_data[0]['data'][i]['short_value'], 2):>7.2f}",
          f"Long:{round(stocks.analytical_data[0]['data'][i]['long_value'], 2):>7.2f}",
          f"Over/Under:", stocks.analytical_data[0]['data'][i]['over_under'], end=' ')
    if 'buy_sell_order' in stocks.analytical_data[0]['data'][i]:
        print("Signal:", stocks.analytical_data[0]['data'][i]['buy_sell_order'],
              f"Purchase Price:{round(stocks.analytical_data[0]['data'][i]['short_value'], 2):>7.2f}")
    else:
        print("")
