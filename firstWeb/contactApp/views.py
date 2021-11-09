from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import EmailMessage


# Create your views here.
def contact_us(request):
    contact_form = ContactForm()
    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            content = request.POST.get('content')

            # e_mail = EmailMessage('App Django Message',
            #                       f'El usuario con nombre {name} y con el mail {email} escribe: \n{content}', '',
            #                       'lolaf@gmail.com', reply_to=None)
            # try:
            #     e_mail.send()
            #     return redirect('/us/?valid')
            #
            # except:
            #     return redirect('/us/?novalid')
            return render(request, 'contactApp/contact_us.html', {'form': contact_form})

# TODO: arreglar que cuando se envía el formulario sale un error de 'this field is required'.
# TODO: arreglar que el formulario no se envía ( url no cambia a ?valid)
