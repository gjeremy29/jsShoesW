from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['name', 'email', 'contact_type', 'ruc', 'direccion', 'message', 'subscription']


