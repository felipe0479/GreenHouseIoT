from .models import Enviroment
from django.utils import timezone
from django.http import HttpResponse

from __future__ import absolute_import
from celery import shared_task

@shared_task
def saveEnv(request):
    var="12,28,52,15,85"
    array=var.split(',')
    temp=array[0]
    alt=array[1]
    air_hum=array[2]
    press=array[3]
    humed=array[4]
    
    if request.method=='GET':
        new=Enviroment(date_now=timezone.now(),ground_humidity=humed,air_humidity=air_hum,temperature=temp,pressure=press,altitude=alt)
        new.save()
    return HttpResponse(status=201)