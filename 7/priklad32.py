#import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/twlo.csv")

import pandas
import matplotlib.pyplot as plt
import datetime as dt

twilio = pandas.read_csv("twlo.csv")
twilio.plot("Date","Close")
#plt.show()

twilio["Date"] = pandas.to_datetime(twilio["Date"])
twilio.plot("Date", "Close")
plt.show()