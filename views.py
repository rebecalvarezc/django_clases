from django.http import HttpResponse


def primera_vista(request):  # a toda función creada dentro del archivo views.py se le denomina "vista"
    return HttpResponse('Bienvenido a mi primera página con Django :)')


def segunda_vista(request):
    return HttpResponse('Hasta luego, gracias por visitar!')
