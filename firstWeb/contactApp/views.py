from django.shortcuts import render
from .forms import ContactForm


# Create your views here.
def contact_us(request):
    contact_form = ContactForm()
    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            content = request.POST.get('content')
    return render(request, 'contactApp/contact_us.html', {'form': contact_form})
