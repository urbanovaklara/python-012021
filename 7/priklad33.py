#import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/7/velikonoce.csv")

import pandas
import matplotlib.pyplot as plt
import datetime as dt

velikonoce = pandas.read_csv("velikonoce.csv")
datumy = dt.strptime(velikonoce["Datum"],"%d.%m.%Y")
print(datumy)