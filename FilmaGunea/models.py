from django.db import models

from django.contrib.auth.models import User

class filmak_bozkatzailea(models.Model):
	 erabiltzailea = models.OneToOneField(User, on_delete=models.CASCADE) 


class filmak_filma(models.Model):
	izenburua = models.CharField(max_length=100)
	zuzendaria = models.CharField(max_length=60)
	urtea = models.IntegerField(max_length=11)
	generoa= models.CharField(max_length=2)
	sipnosia= models.CharField(max_length=500)
	bozkak = models.IntegerField(default=0)
	bozkatzaileak = models.ManyToManyField(filmak_bozkatzailea)
	
