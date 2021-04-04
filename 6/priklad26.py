#import wget

#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_praha.csv")
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_plzeň.csv")
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_liberec.csv")
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/platy_2021_02.csv")

import pandas
from pandas import DataFrame

zam_praha = pandas.read_csv("zam_praha.csv")
zam_liberec = pandas.read_csv("zam_liberec.csv")
zam_plzen = pandas.read_csv("zam_plzeň.csv")

zam_praha["mesto"] = "Praha"
zam_liberec["mesto"] = "Liberec"
zam_plzen["mesto"] = "Plzeň"

zamestnanci = pandas.concat([zam_praha, zam_liberec, zam_plzen], ignore_index=True)
platy = pandas.read_csv("platy_2021_02.csv")
zamestnanci_platy = pandas.merge(zamestnanci, platy, on=["cislo_zamestnance"])
print(zamestnanci.shape)
print(zamestnanci_platy.shape)

prum_plat = zamestnanci_platy.groupby("mesto")["plat"].mean()
print(prum_plat)

