from django import forms


# Create your models here.
class ContactForm(forms.Form):
    name = forms.CharField(label='name', max_length=30)
    email = forms.CharField(label='email', max_length=50)
    content = forms.CharField(label='content', widget=forms.Textarea, required=False)


