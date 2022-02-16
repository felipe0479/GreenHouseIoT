from django.db import models

# Create your models here.
class Enviroment(models.Model):
    date_now=models.DateTimeField()
    ground_humidity=models.CharField(max_length=20, default='DEFAULT VALUE')
    air_humidity=models.CharField(max_length=20, default='DEFAULT VALUE')
    temperature=models.CharField(max_length=20, default='DEFAULT VALUE')
    pressure=models.CharField(max_length=20, default='DEFAULT VALUE')
    altitude=models.CharField(max_length=20, default='DEFAULT VALUE')
    

    
class Devices(models.Model):
    name_device=models.CharField(max_length=100)
    
