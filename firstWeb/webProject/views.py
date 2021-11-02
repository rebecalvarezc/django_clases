from django.shortcuts import render
from servicesApp.models import Service


# Create your views here.

def home(request):
    return render(request, 'webProject/home.html')


def services(request):
    service = Service.objects.all()  # importa todos los servicios que hemos construido
    return render(request, 'webProject/services.html', {'services': service})


def store(request):
    return render(request, 'webProject/store.html')


def contact_us(request):
    return render(request, 'webProject/contact_us.html')


def blog(request):
    return render(request, 'webProject/blog.html')
