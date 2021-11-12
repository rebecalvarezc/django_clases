from django.shortcuts import render
from django.shortcuts import redirect
from .cart import Cart
from storeApp.models import Product, ProdCat


# Create your views here.

def add_product(request, product_id):
    """
    Adds products to our shopping cart using the classes created in StoreApp and here.
    :param request:
    :param product_id:
    :return:
    """

    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.add(product=product)
    return redirect('store')


def delete_product(request, product_id):
    """
    Deletes a product to our shopping cart using the classes created in StoreApp and here.
    :param request:
    :param product_id:
    :return:
    """
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.delete(product=product)
    return redirect('store')


def remove_product(request, product_id):
    """
    Removes a product to our shopping cart using the classes created in StoreApp and here.
    :param request:
    :param product_id:
    :return:
    """

    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.remove(product=product)
    return redirect('store')


def delete_cart(request):
    """
   Deletes all the items in the shopping cart using the classes created in StoreApp and here.
    :param request:
    :return:
    """

    cart = Cart(request)
    cart.clean_cart()
    return redirect('store')