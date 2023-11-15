from django.shortcuts import render
from djangopri.models import Good


def index(request):
    goods = Good.objects.all()
    return render(request, 'index.html', context={'goods':goods, 'name': 'Kio Rio 3'})

def lol(request):
    goods = Good.objects.all()
    return render(request, 'lol.html', context={'goods': goods, 'name': 'Kio Rio 3'})

def Наследование(request):
    goods = Good.objects.all()
    return render(request, 'Наследование.html', context={'goods': goods, 'name': 'Kio Rio 3'})
