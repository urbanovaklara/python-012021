def uspesnostZakazky(odvetvi, obrat, zeme, konference=False, newsletter=False):
    pocetBodu=0
    if odvetvi == "automotive":
        pocetBodu += 3
    elif odvetvi == "retail":
        pocetBodu += 2
    else:
        pocetBodu += 0

    if obrat < 10:
        pocetBodu += 0
    elif obrat < 1000:
        pocetBodu += 3
    else:
        pocetBodu += 1
    if zeme == "Slovensko":
        pocetBodu += 2
    elif zeme=="Česko":
        pocetBodu += 2
    elif zeme == "Francie":
        pocetBodu += 1
    elif zeme=="Německo":
        pocetBodu += 1
    else:
        pocetBodu += 0
    if konference:
        pocetBodu += 1
    else:
        pocetBodu += 0
    if newsletter:
        pocetBodu += 1
    else:
        pocetBodu += 0
    return(pocetBodu)

pocetBodu=uspesnostZakazky("automotive", 9, "Slovensko",newsletter=True)
if pocetBodu <= 5:
    print("Šance na získání zakázky je malá.")
if pocetBodu <= 8:
    print("Šance na získání zakázky je střední.")
else:
    print("Šance na získání zakázky je vysoká.")

