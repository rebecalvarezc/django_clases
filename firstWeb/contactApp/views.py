from django.shortcuts import render
from .forms import ContactForm


# Create your views here.
def contact_us(request):
    contact_form = ContactForm
    return render(request, 'contactApp/contact_us.html', {'form': contact_form})
