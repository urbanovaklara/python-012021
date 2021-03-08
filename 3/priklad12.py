class Auto:
    def get_info(self):
        return f"Jedná se o {self.vozidlo} s registrační značkou {self.regZnacka}."

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

auto1 = Auto("Peugeot 403 Cabrio","4A2 3020",47534)
auto2 = Auto("Škoda Octavia","1P3 4747",41253)

auto=input("Jaké vozidlo si chcete půjčit? Peugeot nebo Škoda?")
if auto=="Peugeot":
    print(auto1.get_info())
    print(auto1.pujc_auto())
elif auto=="Škoda":
    print(auto2.get_info())
    print(auto2.pujc_auto())

auto_zkouska=input("Jaké vozidlo si chcete půjčit?")
if auto=="Peugeot":
    print(auto1.get_info())
    print(auto1.pujc_auto())
elif auto=="Škoda":
    print(auto2.get_info())
    print(auto2.pujc_auto())


