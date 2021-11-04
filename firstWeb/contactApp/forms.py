from django import forms


# Create your models here.
class ContactForm(forms.Form):
    name = forms.CharField(label='name', max_length=30, required=True)
    email = forms.CharField(label='email', max_length=50, required=True)
    content = forms.CharField(label='content', max_length=350)


