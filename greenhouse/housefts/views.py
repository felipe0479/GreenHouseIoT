from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, This is GreenHouseCo")

def showArduino(request):
    import serial
    ser = serial.Serial('/dev/ttyUSB0',9600)
    while True:
        read_serial=ser.readline().decode("utf-8") 
        print (read_serial)
        
        return HttpResponse('<h1>Factores de Ambiente %s prct.</h1>'%read_serial)   
    #return render(request,"housefts/templates/index.html",red_serial)
    
