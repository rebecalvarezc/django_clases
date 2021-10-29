from django.shortcuts import render, HttpResponse


# Create your views here.

def home(request):
    return render(request, 'home.html')


def services(request):
    return render(request, 'services.html')


def store(request):
    return render(request, 'store.html')


def contact_us(request):
    return render(request, 'contact_us.html')


def blog(request):
    return render(request, 'blog.html')
