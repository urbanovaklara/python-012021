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

    def get_celkova_delka(self):
        celkovaDelka = self.delka
        return celkovaDelka

class Serial(Polozka):
    def __init__(self, nazev, zanr, pocetEpisod, delkaEpisody):
        super().__init__(nazev, zanr)
        self.pocetEpisod = pocetEpisod
        self.delkaEpisody = delkaEpisody

    def getInfo(self):
        return f"{super().getInfo()}, Počet episod: {self.pocetEpisod}, Délka jedné episody: {self.delkaEpisody} min."

    def get_celkova_delka(self):
        celkovaDelka = self.pocetEpisod * self.delkaEpisody
        return celkovaDelka

class Uzivatel:
    def __init__(self, uzivatelske_jmeno, delka_sledovani=0):
        self.uzivatelske_jmeno = uzivatelske_jmeno
        self.delka_sledovani = delka_sledovani

    def pripocti_shlednuti(self, celkovaDelka):
        self.delka_sledovani += celkovaDelka

    def getInfo(self):
        return f"Uživatel {self.uzivatelske_jmeno} shlédl {self.delka_sledovani} min."

film1 = Film("Šarlatán", "životopisný/drama", 118)
seriál1 = Serial("Černobyl", "Drama/Historický", 5, 59)
uzivatel1 = Uzivatel("Klára Urbanová")

uzivatel1.pripocti_shlednuti(film1.get_celkova_delka())
uzivatel1.pripocti_shlednuti(seriál1.get_celkova_delka())
print(uzivatel1.getInfo())