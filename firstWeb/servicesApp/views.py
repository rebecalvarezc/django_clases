from django.shortcuts import render
from .models import Service


# Create your views here.
def services(request):
    service = Service.objects.all()  # importa todos los servicios que hemos construido
    return render(request, 'webProject/../templates/services/services.html', {'services': service})
