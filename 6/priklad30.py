import pandas

vykazy = pandas.read_csv("vykazy.csv")
hodin_celkem = vykazy.groupby("project")["hours"].sum()
hodin_celkem.to_excel("vykazane_hodiny.xlsx")

vykazy_excel = pandas.read_excel("vykazane_hodiny.xlsx")
print(vykazy_excel)