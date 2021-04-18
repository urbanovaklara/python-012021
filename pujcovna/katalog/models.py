from django.db import models

# Create your models here.
class Auto(models.Model):
    spz = models.CharField(max_length=7)
    znacka_typ = models.CharField(max_length=50)
    pocet_km_najetych = models.IntegerField()
    technicka_kontrola = models.DateField()

class Zakaznik(models.Model):
    jmeno = models.CharField(max_length=100)
    cislo_rp = models.CharField(max_length=20)
    datum_narozeni = models.DateField()

class Vypujcka(models.Model):
    datum_vypujcky_zac = models.DateTimeField()
    datum_vypujcky_kon = models.DateTimeField()
    cena_vypujcky = models.IntegerField()