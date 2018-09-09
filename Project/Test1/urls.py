from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.http import HttpResponse
from . import views

urlpatterns = [
    path('', views.answer, name='answer'),
    url(r'^Tabla/$', views.Table, name='Table'),
    url(r'^Ingreso/$', views.Ingreso, name='Ingreso'),
    url(r'^IngresoJ/$', views.IngresoJ, name='IngresoJ'),
]
