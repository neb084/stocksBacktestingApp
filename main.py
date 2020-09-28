import constants as c
import functions as f
import datetime
import stock_data

stocks = []
stocks.append(stock_data.Stocks('AAPL'))
print(stocks[0].historical_data)
stocks[0].set_historical_name_hd(0, 'test 1')
print(stocks[0].historical_data)
stocks[0].get_period_type_hd(0)

candles = [{'open': 81.165, 'high': 81.55, 'low': 80.575, 'close': 81.28, 'volume': 104491216, 'datetime': 1591160400000}, {'open': 81.0975, 'high': 81.405, 'low': 80.195, 'close': 80.58, 'volume': 87560364, 'datetime': 1591246800000}, {'open': 80.8375, 'high': 82.9375, 'low': 80.8075, 'close': 82.875, 'volume': 137250200, 'datetime': 1591333200000}, {'open': 82.5625, 'high': 83.4, 'low': 81.83, 'close': 83.365, 'volume': 95654536, 'datetime': 1591592400000}, {'open': 83.035, 'high': 86.4025, 'low': 83.0025, 'close': 85.9975, 'volume': 147712364, 'datetime': 1591678800000}, {'open': 86.975, 'high': 88.6925, 'low': 86.5225, 'close': 88.21, 'volume': 166651752, 'datetime': 1591765200000}, {'open': 87.3275, 'high': 87.765, 'low': 83.87, 'close': 83.975, 'volume': 201662452, 'datetime': 1591851600000}, {'open': 86.18, 'high': 86.95, 'low': 83.555825, 'close': 84.7, 'volume': 200146052, 'datetime': 1591938000000}, {'open': 83.3125, 'high': 86.42, 'low': 83.145, 'close': 85.7475, 'volume': 138808920, 'datetime': 1592197200000}, {'open': 87.865, 'high': 88.3, 'low': 86.18, 'close': 88.02, 'volume': 165428728, 'datetime': 1592283600000}, {'open': 88.7875, 'high': 88.85, 'low': 87.7725, 'close': 87.8975, 'volume': 114406504, 'datetime': 1592370000000}, {'open': 87.8525, 'high': 88.3625, 'low': 87.305, 'close': 87.9325, 'volume': 96820384, 'datetime': 1592456400000}, {'open': 88.65875, 'high': 89.14, 'low': 86.2875, 'close': 87.43, 'volume': 264475808, 'datetime': 1592542800000}, {'open': 87.835, 'high': 89.865, 'low': 87.7875, 'close': 89.7175, 'volume': 135445264, 'datetime': 1592802000000}, {'open': 91.0, 'high': 93.095, 'low': 90.567525, 'close': 91.6325, 'volume': 212155476, 'datetime': 1592888400000}, {'open': 91.25, 'high': 92.1975, 'low': 89.63, 'close': 90.015, 'volume': 192623396, 'datetime': 1592974800000}, {'open': 90.175, 'high': 91.25, 'low': 89.3925, 'close': 91.21, 'volume': 137522512, 'datetime': 1593061200000}, {'open': 91.1025, 'high': 91.33, 'low': 88.255, 'close': 88.4075, 'volume': 205256844, 'datetime': 1593147600000}, {'open': 88.3125, 'high': 90.5434, 'low': 87.82, 'close': 90.445, 'volume': 130646076, 'datetime': 1593406800000}, {'open': 90.02, 'high': 91.495, 'low': 90.0, 'close': 91.2, 'volume': 140223284, 'datetime': 1593493200000}, {'open': 91.28, 'high': 91.84, 'low': 90.9775, 'close': 91.0275, 'volume': 110737236, 'datetime': 1593579600000}, {'open': 91.9625, 'high': 92.6175, 'low': 90.91, 'close': 91.0275, 'volume': 114041468, 'datetime': 1593666000000}, {'open': 92.5, 'high': 93.945, 'low': 92.4675, 'close': 93.4625, 'volume': 118655652, 'datetime': 1594011600000}, {'open': 93.8525, 'high': 94.655, 'low': 93.0575, 'close': 93.1725, 'volume': 112424456, 'datetime': 1594098000000}, {'open': 94.18, 'high': 95.375, 'low': 94.09, 'close': 95.3425, 'volume': 117091880, 'datetime': 1594184400000}, {'open': 96.2625, 'high': 96.3175, 'low': 94.6725, 'close': 95.6825, 'volume': 125642608, 'datetime': 1594270800000}, {'open': 95.335, 'high': 95.98, 'low': 94.705175, 'close': 95.92, 'volume': 90257320, 'datetime': 1594357200000}, {'open': 97.265, 'high': 99.955, 'low': 95.2575, 'close': 95.4775, 'volume': 191649140, 'datetime': 1594616400000}, {'open': 94.84, 'high': 97.255, 'low': 93.8775, 'close': 97.0575, 'volume': 170989364, 'datetime': 1594702800000}, {'open': 98.99, 'high': 99.2475, 'low': 96.49, 'close': 97.725, 'volume': 153197932, 'datetime': 1594789200000}, {'open': 96.5625, 'high': 97.405, 'low': 95.905, 'close': 96.5225, 'volume': 110577672, 'datetime': 1594875600000}, {'open': 96.9875, 'high': 97.1475, 'low': 95.84, 'close': 96.3275, 'volume': 92186900, 'datetime': 1594962000000}, {'open': 96.41625, 'high': 98.5, 'low': 96.0625, 'close': 98.3575, 'volume': 90317908, 'datetime': 1595221200000}, {'open': 99.1725, 'high': 99.25, 'low': 96.7425, 'close': 97.0, 'volume': 103645836, 'datetime': 1595307600000}, {'open': 96.6925, 'high': 97.975, 'low': 96.6025, 'close': 97.2725, 'volume': 89001652, 'datetime': 1595394000000}, {'open': 96.998375, 'high': 97.0775, 'low': 92.00975, 'close': 92.845, 'volume': 197004432, 'datetime': 1595480400000}, {'open': 90.9875, 'high': 92.97, 'low': 89.145, 'close': 92.615, 'volume': 185438864, 'datetime': 1595566800000}, {'open': 93.71, 'high': 94.905, 'low': 93.48, 'close': 94.81, 'volume': 121214192, 'datetime': 1595826000000}, {'open': 94.3675, 'high': 94.54965, 'low': 93.2475, 'close': 93.2525, 'volume': 103625500, 'datetime': 1595912400000}, {'open': 93.75, 'high': 95.23, 'low': 93.7125, 'close': 95.04, 'volume': 90329256, 'datetime': 1595998800000}, {'open': 94.1875, 'high': 96.2975, 'low': 93.7675, 'close': 96.19, 'volume': 158130020, 'datetime': 1596085200000}, {'open': 102.88375, 'high': 106.415, 'low': 100.825, 'close': 106.26, 'volume': 374295468, 'datetime': 1596171600000}, {'open': 108.2, 'high': 111.636425, 'low': 107.8925, 'close': 108.9375, 'volume': 308151388, 'datetime': 1596430800000}, {'open': 109.1325, 'high': 110.79, 'low': 108.3875, 'close': 109.665, 'volume': 172792368, 'datetime': 1596517200000}, {'open': 109.3775, 'high': 110.3925, 'low': 108.8975, 'close': 110.0625, 'volume': 121991952, 'datetime': 1596603600000}, {'open': 110.405, 'high': 114.4125, 'low': 109.7975, 'close': 113.9025, 'volume': 202428900, 'datetime': 1596690000000}, {'open': 113.205, 'high': 113.675, 'low': 110.2925, 'close': 111.1125, 'volume': 198045612, 'datetime': 1596776400000}, {'open': 112.6, 'high': 113.775, 'low': 110.0, 'close': 112.7275, 'volume': 212403424, 'datetime': 1597035600000}, {'open': 111.96875, 'high': 112.4825, 'low': 109.106675, 'close': 109.375, 'volume': 187902376, 'datetime': 1597122000000}, {'open': 110.4975, 'high': 113.275, 'low': 110.2975, 'close': 113.01, 'volume': 165944820, 'datetime': 1597208400000}, {'open': 114.43, 'high': 116.0425, 'low': 113.9275, 'close': 115.01, 'volume': 210082064, 'datetime': 1597294800000}, {'open': 114.82875, 'high': 115.0, 'low': 113.045, 'close': 114.9075, 'volume': 165565208, 'datetime': 1597381200000}, {'open': 116.0625, 'high': 116.0875, 'low': 113.962525, 'close': 114.6075, 'volume': 119561444, 'datetime': 1597640400000}, {'open': 114.3525, 'high': 116.0, 'low': 114.0075, 'close': 115.5625, 'volume': 105633540, 'datetime': 1597726800000}, {'open': 115.98325, 'high': 117.1625, 'low': 115.61, 'close': 115.7075, 'volume': 145538008, 'datetime': 1597813200000}, {'open': 115.75, 'high': 118.392, 'low': 115.733375, 'close': 118.275, 'volume': 126907188, 'datetime': 1597899600000}, {'open': 119.2625, 'high': 124.868, 'low': 119.25, 'close': 124.37, 'volume': 338054640, 'datetime': 1597986000000}, {'open': 128.6975, 'high': 128.785, 'low': 123.93625, 'close': 125.8575, 'volume': 345937768, 'datetime': 1598245200000}, {'open': 124.6975, 'high': 125.1793, 'low': 123.0525, 'close': 124.825, 'volume': 211495788, 'datetime': 1598331600000}, {'open': 126.179125, 'high': 126.9925, 'low': 125.0825, 'close': 126.5225, 'volume': 163022268, 'datetime': 1598418000000}, {'open': 127.1425, 'high': 127.485, 'low': 123.8325, 'close': 125.01, 'volume': 155552384, 'datetime': 1598504400000}, {'open': 126.0125, 'high': 126.4425, 'low': 124.5775, 'close': 124.8075, 'volume': 187629916, 'datetime': 1598590800000}, {'open': 127.58, 'high': 131.0, 'low': 126.0, 'close': 129.04, 'volume': 225702690, 'datetime': 1598850000000}, {'open': 132.76, 'high': 134.8, 'low': 130.53, 'close': 134.18, 'volume': 152470140, 'datetime': 1598936400000}, {'open': 137.59, 'high': 137.98, 'low': 127.0, 'close': 131.4, 'volume': 200118990, 'datetime': 1599022800000}, {'open': 126.91, 'high': 128.84, 'low': 120.5, 'close': 120.88, 'volume': 257599640, 'datetime': 1599109200000}, {'open': 120.07, 'high': 123.7, 'low': 110.89, 'close': 120.96, 'volume': 332607160, 'datetime': 1599195600000}, {'open': 113.95, 'high': 118.99, 'low': 112.68, 'close': 112.82, 'volume': 231366560, 'datetime': 1599541200000}, {'open': 117.26, 'high': 119.14, 'low': 115.26, 'close': 117.32, 'volume': 176940460, 'datetime': 1599627600000}, {'open': 120.36, 'high': 120.5, 'low': 112.5, 'close': 113.49, 'volume': 182274390, 'datetime': 1599714000000}, {'open': 114.57, 'high': 115.23, 'low': 110.0, 'close': 112.0, 'volume': 180860330, 'datetime': 1599800400000}, {'open': 114.72, 'high': 115.93, 'low': 112.8, 'close': 115.355, 'volume': 140150090, 'datetime': 1600059600000}, {'open': 118.33, 'high': 118.829, 'low': 113.61, 'close': 115.54, 'volume': 184642040, 'datetime': 1600146000000}, {'open': 115.23, 'high': 116.0, 'low': 112.04, 'close': 112.13, 'volume': 155026680, 'datetime': 1600232400000}, {'open': 109.72, 'high': 112.2, 'low': 108.71, 'close': 110.34, 'volume': 178010970, 'datetime': 1600318800000}, {'open': 110.4, 'high': 110.88, 'low': 106.09, 'close': 106.84, 'volume': 287104880, 'datetime': 1600405200000}, {'open': 104.54, 'high': 110.19, 'low': 103.1, 'close': 110.08, 'volume': 195713820, 'datetime': 1600664400000}, {'open': 112.68, 'high': 112.86, 'low': 109.16, 'close': 111.81, 'volume': 183055370, 'datetime': 1600750800000}, {'open': 111.62, 'high': 112.11, 'low': 106.77, 'close': 107.12, 'volume': 150718670, 'datetime': 1600837200000}, {'open': 105.17, 'high': 110.25, 'low': 105.0, 'close': 108.22, 'volume': 167743350, 'datetime': 1600923600000}, {'open': 108.43, 'high': 112.44, 'low': 107.67, 'close': 112.28, 'volume': 149981440, 'datetime': 1601010000000}]
print(len(candles))
stocks[0].set_candles_hd(0, candles)
stocks[0].get_candles_hd(0)
