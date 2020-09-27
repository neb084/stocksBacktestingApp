import constants as c
import functions as f
import datetime

historical_data = []
historical_data.append({'historical_name': 'test1', 'start_datetime': 1, 'end_datetime': 2, 'period': 1,
                        'frequency_type': 'daily', 'frequency': 1, 'extended_hours': 'false', 'candles': []})
historical_data[0]['candles'].append({'datetime': 123, 'open': 50, 'close': 48.5, 'high': 50.2, 'low': 47.9})
historical_data[0]['candles'].append({'datetime': 523, 'open': 49, 'close': 47.5, 'high': 50.0, 'low': 45.9})

print(historical_data)

analysis_data = []
analysis_data.append({'analysis_name': 'analysis1', 'historical_name_reference': 'test1',
                      'buy_signal': 'OPEN_NEXT_DAY', 'sell_signal': 'CLOSE_SAME_DAY', 'analysis_type': 'MA',
                      'short_ma_type': 'EMA', 'short_ma_length': 9, 'long_ma_type': 'SMA', 'long_ma_length': 20,
                      'data': []})
analysis_data[0]['data'].append({'short_value': 50, 'long_value': 48, 'over_under': c.OVER, 'signal': 'BUY'})

