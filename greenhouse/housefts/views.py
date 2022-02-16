from cmath import sin
import io
import matplotlib.pyplot as plt
from django.http import HttpResponse
from django.shortcuts import render
from matplotlib.backends.backend_agg import FigureCanvasAgg
from django.utils import timezone

# Elementos necesarios para que el API REST funcione 
from rest_framework import viewsets
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from django.views.generic.edit import CreateView

from django.contrib import messages 
from django.contrib.messages.views import SuccessMessageMixin 

from housefts.serializers import EnviromentSerializer

from random import sample
 
# Modelo 'Enviroment' 
from housefts.models import Enviroment

class SaveEnviroment(SuccessMessageMixin, CreateView): 
    model = Enviroment
    form = Enviroment
    fields = "__all__" 
    success_message = 'Datos registrados existosamente'     
 
class EnviromentViewSet(viewsets.ModelViewSet):    
    
    queryset = Enviroment.objects.all().order_by('id')
    serializer_class = EnviromentSerializer

# Create your views here.
def saveEnv(request):
    var="35,953,84,668,75"
    array=var.split(',')
    temp=array[0]
    alt=array[1]
    air_hum=array[2]
    press=array[3]
    humed=array[4]
    
    if request.method=='GET':
        new=Enviroment(date_now=timezone.now(),ground_humidity=humed,air_humidity=air_hum,temperature=temp,pressure=press,altitude=alt)
        new.save()
    last=Enviroment.objects.last().__dict__
    return render(request, 'house/index.html', 
    {'temp':last['temperature'],
    'alt':last['altitude'],
    'press':last['pressure'],
    'humed':last['ground_humidity'],
    'air_hum':last['air_humidity']})

def index(request):
    objects=Enviroment.objects.all()
    return render(request,'house/history.html',{'objects':objects})

def showArduino(request):
    import serial
    ser = serial.Serial('/dev/ttyUSB0',9600)
    while True:
        read_serial=ser.readline().decode("utf-8") 
        print (read_serial)
        
        return HttpResponse('<h1>Factores de Ambiente %s prct.</h1>'%read_serial)   
    #return render(request,"housefts/templates/index.html",red_serial)
def plot(request):
    # Creamos los datos para representar en el gráfico
    temp=[]
    humed=[]
    press=[]
    air_hum=[]
    alt=[]
    objects=Enviroment.objects.all()
    for var in objects:
        temp += [var.temperature]
        humed += [var.ground_humidity]
        press += [var.pressure]
        air_hum += [var.air_humidity]
        alt += [var.altitude]
    x = range(len(temp))
    
   

    # Creamos una figura y le dibujamos el gráfico
    f = plt.figure(figsize=(8,12))

    # Creamos los ejes
    #axes = f.add_axes([0.15, 0.15, 0.75, 0.75]) # [left, bottom, width, height]
    axes1=f.add_subplot(321)
    axes1.plot(x, temp,label='temperatura',color='orange')
    axes1.set_title("Temperatura")

    axes2=f.add_subplot(322)
    axes2.plot(x,humed,label='humedad tierra',color="brown")
    axes2.set_title("Humedad Tierra")

    axes3=f.add_subplot(323)
    axes3.plot(x,air_hum,label='humedad aire')
    axes3.set_title("Humedad Aire")

    axes4=f.add_subplot(324)
    axes4.plot(x,press,label='presión atm',color="purple")
    axes4.set_title("Presión Atm")

    axes5=f.add_subplot(325)
    axes5.plot(x,alt,label='altitud',color="red")
    axes5.set_title("Altitud")

    #axes.set_xlabel("Tiempo")
    #axes.set_ylabel("Variables de Entorno")
    #axes.set_title("GreenHouse Co")
    #axes.legend()
    f.suptitle("Varibles de Entorno GreenHouse Co")

    # Como enviaremos la imagen en bytes la guardaremos en un buffer
    buf = io.BytesIO()
    canvas = FigureCanvasAgg(f)
    canvas.print_png(buf)

    # Creamos la respuesta enviando los bytes en tipo imagen png
    response = HttpResponse(buf.getvalue(), content_type='image/png')

    # Limpiamos la figura para liberar memoria
    f.clear()

    # Añadimos la cabecera de longitud de fichero para más estabilidad
    response['Content-Length'] = str(len(response.content))

    # Devolvemos la response
    return response

def date_plot(request,firstdate,lastdate):
    # Creamos los datos para representar en el gráfico
    temp=[]
    humed=[]
    press=[]
    air_hum=[]
    alt=[]
    objects=Enviroment.objects.all()
    for var in objects:
        temp += [var.temperature]
        humed += [var.ground_humidity]
        press += [var.pressure]
        air_hum += [var.air_humidity]
        alt += [var.altitude]
    x = range(len(temp))
    
   

    # Creamos una figura y le dibujamos el gráfico
    f = plt.figure(figsize=(8,12))

    # Creamos los ejes
    #axes = f.add_axes([0.15, 0.15, 0.75, 0.75]) # [left, bottom, width, height]
    axes1=f.add_subplot(321)
    axes1.plot(x, temp,label='temperatura',color='orange')
    axes1.set_title("Temperatura")

    axes2=f.add_subplot(322)
    axes2.plot(x,humed,label='humedad tierra',color="brown")
    axes2.set_title("Humedad Tierra")

    axes3=f.add_subplot(323)
    axes3.plot(x,air_hum,label='humedad aire')
    axes3.set_title("Humedad Aire")

    axes4=f.add_subplot(324)
    axes4.plot(x,press,label='presión atm',color="purple")
    axes4.set_title("Presión Atm")

    axes5=f.add_subplot(325)
    axes5.plot(x,alt,label='altitud',color="red")
    axes5.set_title("Altitud")

    #axes.set_xlabel("Tiempo")
    #axes.set_ylabel("Variables de Entorno")
    #axes.set_title("GreenHouse Co")
    #axes.legend()
    f.suptitle("Varibles de Entorno GreenHouse Co")

    # Como enviaremos la imagen en bytes la guardaremos en un buffer
    buf = io.BytesIO()
    canvas = FigureCanvasAgg(f)
    canvas.print_png(buf)

    # Creamos la respuesta enviando los bytes en tipo imagen png
    response = HttpResponse(buf.getvalue(), content_type='image/png')

    # Limpiamos la figura para liberar memoria
    f.clear()

    # Añadimos la cabecera de longitud de fichero para más estabilidad
    response['Content-Length'] = str(len(response.content))

    # Devolvemos la response
    return response
    
