from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Profil(models.Model):
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    ersteller = models.CharField(max_length=10)

    def __str__(self):
        return self.ersteller


class Anleitung(models.Model):
    profil = models.ForeignKey(Profil, on_delete=models.RESTRICT)
    anleittitel = models.CharField(max_length=100)
    ersteller = models.CharField(max_length=100)
    kategorie = models.CharField(max_length=100)
    dauer = models.DurationField()
    datum = models.DateField('datum_erstellt')
    img = models.ImageField(upload_to='images/thumbnail', default=None)

    def __str__(self):
        return self.anleittitel


class Anleitungsschritt(models.Model):
    anleitung = models.ForeignKey(Anleitung, on_delete=models.CASCADE)
    schrittbenennung = models.CharField(max_length=50)
    beschreibung = models.CharField(max_length=500)
    schrittbild = models.ImageField(upload_to='images/Schrittbilder/', default=None)
    
    def __str__(self):
        return self.schrittbenennung
    

class Komponente(models.Model):
    anleitungsschritt = models.ForeignKey(Anleitungsschritt, on_delete=models.CASCADE)
    kompbeschreibung = models.CharField(max_length=100)
    kompbild = models.ImageField(upload_to='images/Komponentenbilder', default=None)

    def __str__(self):
        return self.kompbeschreibung

