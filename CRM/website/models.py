from django.db import models

# Create your models here.


class kayit(models.Model):
	created_at = models.DateField(auto_now_add=True)
	isim = models.CharField(max_length=150)
	soyisim = models.CharField(max_length=150)
	adres = models.CharField(max_length=150)
	il = models.CharField(max_length=150)
	ilce = models.CharField(max_length=150)
	postakod = models.CharField(max_length=10)
	email = models.CharField(max_length=150)
	telefon = models.CharField(max_length=13)

	def __str__(self):
		return (f"{self.isim} {self.soyisim}")
