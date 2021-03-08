vysledky = [
  {"Jméno": "Mirek Dušín", "Český jazyk": 1, "Anglický jazyk": 2, "Matematika": 1, "Biologie": 1, "Zeměpis": 1},
  {"Jméno": "Jarka Metelka", "Český jazyk": 3, "Anglický jazyk": 1, "Matematika": 3, "Dějepis": 2, "Ekonomika": 5},
  {"Jméno": "Jindra Hojer", "Český jazyk": 2, "Anglický jazyk": 2, "Matematika": 1, "Biologie": 3, "Chemie": 3},
  {"Jméno": "Červenáček", "Český jazyk": 1, "Anglický jazyk": 1, "Matematika": 1, "Fyzika": 2, "Informatika": 4},
  {"Jméno": "Rychlonožka", "Český jazyk": 4, "Anglický jazyk": 3, "Matematika": 2, "Chemie": 1, "Biologie": 4},
]
prumerZnamek=0
for item in vysledky:
  for key, value in item.items():
    prumerZnamek=item["Český jazyk"]+item["Anglický jazyk"]+["Matematika"]+["Biologie"]+item["Zeměpis"]+item["Dějepis"]+item["Ekonomika"]+item["Chemie"]+item["Informatika"]+item["Fyzika"]
  print(item["Jméno"],prumerZnamek)


