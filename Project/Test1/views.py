from django.shortcuts import render
from django.http import HttpResponse
from .models import Carnet
from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.

# Recibe y envia consultas (GET)
def answer(request):
    send = ("yas")
    return HttpResponse(send)

@csrf_exempt
def Ingreso(request):
    response = int(request.read())
    response += 1000 
    return HttpResponse(response ," te dio!")

@csrf_exempt #JSON
def IngresoJ(request):
    response = json.loads(request.body.decode("utf-8"))
    Hai = int(response['Number'])+1000
    return HttpResponse(Hai ," te dio!")

def Table(request):
    Table,err = Carnet.objets.all()
    if err == Null:
        err = "No hay nada"
        return HttpResponse(err)
    return HttpResponse(Table)