from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from orders.models import Goods
from django.conf import settings


# Create your views here.

def search_product(request):
    return render(request, 'products.html')


def search(request):
    if request.GET["product"]:
        product = request.GET['product']
        goods = Goods.objects.filter(name__icontains=product)
        # buscar __icontains en la documentación de Django. Funciona como el LIKE (%x%) en SQL.
        # message = f'Product searched: {product}'
        return render(request, 'search_results.html', {'goods': goods, 'query': product})
    else:
        message = 'The search field is empty. Try again.'
    return HttpResponse(message)


def contact(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message'] + request.POST['e-mail']
        email_from = settings.EMAIL_HOST_USER
        # especificamos de donde viene el e-mail (de la dirección indicada en settings.py)
        recipient_list = ['correo al que quiero que llegue el form']
        send_mail(subject, message, email_from, recipient_list)
        return HttpResponse('<html><body><h1> Thanks! </h1></body></html>')
    return render(request, 'contact.html')
