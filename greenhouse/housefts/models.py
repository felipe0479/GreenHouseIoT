from django.db import models

# Create your models here.
class Enviroment(models.Model):
    ground_humidity=models.CharField(max_length=30)
    air_humidity=models.CharField(max_length=30)
    temperature=models.CharField(max_length=30)
    date_now=models.DateTimeField()
    
class Devices(models.Model):
    name_device=models.CharField(max_length=100)
    
