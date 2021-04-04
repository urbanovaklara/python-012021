#import wget

#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/staty.json")
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/gdp.csv")

import pandas

staty = pandas.read_json("staty.json")

staty_evropa = staty[staty["region"] == "Europe"]

pocet_statu_subregiony = staty_evropa.groupby("subregion")["name"].count()
print(pocet_statu_subregiony)

pocet_statu_subregiony = staty_evropa.groupby("subregion")["population"].sum()
print(pocet_statu_subregiony)

