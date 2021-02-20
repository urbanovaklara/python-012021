sklad = {
    "1N4148": 250,
    "BAV21": 54,
    "KC147": 147,
    "2N7002": 97,
    "BC547C": 10
}

kod_soucastky = input("Jaký je kód součástky?")
pozadovane_mnozstvi = int(input("Jaké je požadované množství součástky?"))

if not kod_soucastky in sklad:
    print("Není skladem")
elif pozadovane_mnozstvi < sklad[kod_soucastky]:
    print("Poptávku lze uspokojit v plné výši")
    sklad[kod_soucastky] = sklad[kod_soucastky] - pozadovane_mnozstvi
elif pozadovane_mnozstvi > sklad[kod_soucastky]:
    print("Poptávku lze uspokojit pouze částečně")
    sklad.pop(kod_soucastky)
