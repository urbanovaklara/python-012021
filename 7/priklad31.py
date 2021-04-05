#import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")

import pandas
temperatures = pandas.read_csv("temperature.csv")

teploty_17 = temperatures[temperatures["Day"] == 13]
teploty_odmaz = temperatures[temperatures["AvgTemperature"] != -99]
teploty_odmaz.sort_values(by="AvgTemperature", ascending=False)
print(teploty_odmaz.iloc[:4])
print(teploty_odmaz.iloc[-4:])