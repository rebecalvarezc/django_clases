from django.shortcuts import render
from .models import Product


# Create your views here.

def store(request):
    product = Product.objects.all()
    return render(request, 'store/store.html', {'products': product})
