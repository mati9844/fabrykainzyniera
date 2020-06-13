from datetime import date, datetime

from django.db import models

# Create your models here.
from django.conf import settings


class Wydzial(models.Model):
    nazwa_wydzial = models.CharField(max_length=200)

    def __str__(self):
        return str(self.nazwa_wydzial)


class Uczen(models.Model):
    imie_uczen = models.CharField(max_length=200)
    nazwisko_uczen = models.CharField(max_length=200)
    indeks_uczen = models.IntegerField(default=0)
    wydzial_uczen = models.ForeignKey('Wydzial', on_delete=models.CASCADE)

    def __str__(self):
        s = str(self.imie_uczen) + ' ' + str(self.nazwisko_uczen) + \
            ' ' + str(self.indeks_uczen)
        return s


# to delete but have to recreate database/migrations
class Opiekun(models.Model):
    imie_opiekun = models.CharField(max_length=200)
    nazwisko_opiekun = models.CharField(max_length=200)

    def __str__(self):
        s = str(self.imie_opiekun) + ' ' + \
            str(self.nazwisko_opiekun) + ' ' + str(self.indeks_opiekun)
        return s
#


class Praca(models.Model):
    temat_praca = models.CharField(max_length=200)

    def __str__(self):
        s = str(self.temat_praca)
        return s


class ListaPrac(models.Model):
    temat_praca = models.ForeignKey('Praca', on_delete=models.CASCADE)
    uczen_praca = models.ForeignKey(
        Uczen, on_delete=models.CASCADE, blank=True, null=True)
    termin_praca = models.DateTimeField(default=datetime.now, blank=True)
    opiekun_praca = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        s = str(self.temat_praca) + ' ' + str(self.uczen_praca) + \
            ' ' + str(self.termin_praca)
        return s
