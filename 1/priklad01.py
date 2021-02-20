baliky = {
    "B541X": True,
    "B547X": False,
    "B251X": False,
    "B501X": True,
    "B947X": False,
}

cislo_baliku=input("Zadej číslo balíku")

if baliky[cislo_baliku]:
    print("Balík byl předán kurýrovi")
else:
    print("Balík zatím nebyl předán kurýrovi")