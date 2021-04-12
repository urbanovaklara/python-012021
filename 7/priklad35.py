import pandas
import matplotlib.pyplot as plt

temperatures = pandas.read_csv("temperature.csv")
teploty_vybrane = temperatures[temperatures["City"].isin(["Helsinki", "Miami Beach", "Tokyo"])]
teploty_vybrane = teploty_vybrane[["City", "AvgTemperature"]]

helsinki = temperatures[temperatures["City"] == "Helsinki"]
miami = temperatures[temperatures["City"] == "Miami Beach"]
tokyo = temperatures[temperatures["City"] == "Tokyo"]
teploty_vybrane["Helsinki"] = helsinki["AvgTemperature"]
teploty_vybrane["Miami Beach"] = miami["AvgTemperature"]
teploty_vybrane["Tokyo"] = tokyo["AvgTemperature"]
teploty_vybrane[["Helsinki", "Miami Beach", "Tokyo"]].plot(kind="box",whis=[0,100])
plt.show()
