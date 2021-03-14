from datetime import datetime, date

class Kontakt:
    def __init__(self, jmeno, email):
        self.jmeno = jmeno
        self.email = email

class Uchazec(Kontakt):
    def __init__(self, jmeno, email, datum_pohovoru, zapis_z_pohovoru=""):
        super().__init__(jmeno, email)
        self.datum_pohovoru = datetime.strptime(datum_pohovoru,"%d.%m.%Y")

    def uloz_zapis(self):
        today = datetime.today()
        if today < self.datum_pohovoru:
            return f"Zápis z pohovoru je ukládán k uchazeči, s nímž pohovor ještě neproběhl."
        else:
            zapis_z_pohovoru = input(str("Vložte zápis z pohovoru:"))
            return f"Zápis byl uložen"

uchazec1 = Uchazec ("Klára Urbanová", "klara@seznam.cz", "22.2.2021")
print(uchazec1.uloz_zapis())

