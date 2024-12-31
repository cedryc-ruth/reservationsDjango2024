from django.db import models

# Create your models here.
class Locality(models.Model):
	postal_code = models.CharField(max_length=6)
	locality = models.CharField(max_length=30)
	
	class Meta:
		db_table = "localities"
