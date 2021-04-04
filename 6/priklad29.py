#import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")

import pandas
temperatures = pandas.read_csv("temperature.csv")

teploty_17 = temperatures[temperatures["Day"] == 13]

teploty_odmaz = temperatures[temperatures["AvgTemperature"] != -99]

teploty_pocty = temperatures.groupby("Region")["Region"].count()

teplota_prum = temperatures.groupby("Region")["AvgTemperature"].mean()

teplota_max = temperatures.groupby("Region")["AvgTemperature"].max()

teplota_min = temperatures.groupby("Region")["AvgTemperature"].min()



