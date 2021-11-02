from django.shortcuts import render
from .models import Service


# Create your views here.
def services(request):
    service = Service.objects.all()  # importa todos los servicios que hemos construido
    return render(request,
                  'C:/Users/Rebeca/PycharmProjects/djangoProject/firstWeb/servicesApp/templates/services/services.html',
                  # No puedo usar 'serviceApp/services.html'
                  {'services': service})
