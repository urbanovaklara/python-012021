#import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/7/velikonoce.csv")

import pandas
import matplotlib.pyplot as plt
import datetime as dt

velikonoce = pandas.read_csv("velikonoce.csv")
ax = velikonoce.plot("Datum", "Počet", kind="bar")
ax.set_ylabel("Počet dnů")
ax.set_xlabel("Datum")
ax.set_title("Kolikrát připadly Velikonoce na konkrétní datum mezi lety 1600 až 2100")

plt.show()