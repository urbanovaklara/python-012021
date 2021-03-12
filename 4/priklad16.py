class Polozka:
    def __init__(self, nazev, zanr):
        self.nazev = nazev
        self.zanr = zanr

    def getInfo(self):
        return f"Název:{self.nazev}, Žánr: {self.zanr}"

class Film(Polozka):
    def __init__(self, nazev, zanr, delka):
        super().__init__(nazev, zanr)
        self.delka = delka

    def getInfo(self):
        return f"{super().getInfo()}, Délka filmu: {self.delka} min."


class Serial(Polozka):
    def __init__(self, nazev, zanr, pocetEpisod, delkaEpisody):
        super().__init__(nazev, zanr)
        self.pocetEpisod = pocetEpisod
        self.delkaEpisody = delkaEpisody

    def getInfo(self):
        return f"{super().getInfo()}, Počet episod: {self.pocetEpisod}, Délka jedné episody: {self.delkaEpisody} min."

film1 = Film("Šarlatán", "životopisný/drama", 118)
seriál1 = Serial("Černobyl", "Drama/Historický", 5, 59)
print(film1.getInfo())
print(seriál1.getInfo())