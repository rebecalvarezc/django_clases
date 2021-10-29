from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'webProject/home.html')


def services(request):
    return render(request, 'webProject/services.html')


def store(request):
    return render(request, 'webProject/store.html')


def contact_us(request):
    return render(request, 'webProject/contact_us.html')


def blog(request):
    return render(request, 'webProject/blog.html')
