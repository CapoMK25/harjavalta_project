from django.db import models

# Create your models here.

class Jobs(models.Model):
    nimi = models.CharField(max_length=100)
    kuvaus = models.TextField()
    sijainti = models.CharField(max_length=100)
    yritys = models.CharField(max_length=100)
    palkka = models.CharField(max_length=50, blank=True)
    julkistuspäivämäärä = models.DateField()

    def __str__(self):
        return self.nimi  # Changed from self.title to self.nimi