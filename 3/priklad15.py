from datetime import datetime, timedelta
datumNavstevy = datetime.strptime(input("Zadejte datum návštěvy kina."),"%d.%m.%Y")


if datumNavstevy < datetime(2021, 7, 1) or datumNavstevy > datetime(2021, 8, 31):
    print("V této době je letní kino zavřené.")
elif datumNavstevy > datetime(2021, 7, 1) or datumNavstevy <= datetime(2021, 8, 10):
    pocetOsob = int(input("Zadejte počet lístků."))
    cenaCelkem = pocetOsob * 250
    print (f"Celková cena za vstupenky je {cenaCelkem}")
elif datumNavstevy >= datetime(2021, 8, 11) or datumNavstevy <= datetime(2021, 8, 31):
    pocetOsob = int(input("Zadejte počet lístků."))
    cenaCelkem = pocetOsob * 180
    print (f"Celková cena za vstupenky je {cenaCelkem}")