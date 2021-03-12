class Auto:
    def get_info(self):
        return f"Jedná se o {self.vozidlo} s registrační značkou {self.regZnacka} a má najeto {self.pocetKilometru}. Volne:{self.volne}"

    def __init__(self, vozidlo, regZnacka, pocetKilometru, volne=True):
        self.vozidlo=vozidlo
        self.regZnacka=regZnacka
        self.pocetKilometru=pocetKilometru
        self.volne=True

    def pujc_auto(self):
        if self.volne:
            self.volne = False
            return "Potvrzuji zapůjčení vozidla."
        else:
            return "Vozidlo není k dispozici."
    def vrat_auto(self, stavTachometru, pocetDni):
        self.volne = True
        self.pocetDni = pocetDni
        self.stavTachometru = stavTachometru
        self.pocetKilometru += stavTachometru

        if pocetDni <= 7:
            return f"Cena za půjčení auta je {pocetDni * 400} Kč."
        else:
            return f"Cena za půjčení auta je {pocetDni * 300} Kč."


auto1 = Auto("Peugeot 403 Cabrio","4A2 3020",10000)
auto2 = Auto("Škoda Octavia","1P3 4747",20000)


print(auto1.vrat_auto(int(input("Kolik km jste s autem najel?")),int(input("Kolik dní jste měl auto půjčené?"))))
