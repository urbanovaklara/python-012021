def kontrolaCisla(telCislo):
    telCislo = telCislo.replace("+420","")
    telCislo = telCislo.replace(" ", "")

    if len(telCislo)==9:
        textZpravy=input("Zde vložte text zprávy:")
        pocetZnaku=len(textZpravy)
        cenaPom=int(pocetZnaku/180)
        cena=3+(cenaPom*3)
        print(f"Cena za sms je {cena} Kč.")
    else:
        print("Chybné telefonní číslo!")

kontrolaCisla("+420 723 949 229")
