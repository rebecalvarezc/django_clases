from django.shortcuts import render, HttpResponse


# Create your views here.

def home(request):
    return HttpResponse('home')


def services(request):
    return HttpResponse('services')


def store(request):
    return HttpResponse('store')


def contact_us(request):
    return HttpResponse('contact us')


def blog(request):
    return HttpResponse('blog')
