from django.contrib import admin
from django.urls import path
from djangopri.views import index, lol, Наследование

urlpatterns = [
    path('index', index),
    path('lol', lol),
    path('Наследование', Наследование)
]