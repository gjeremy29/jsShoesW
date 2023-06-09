from django import forms

class ContactForm(forms.Form):
    nombres = forms.CharField(max_length=100, required=True)
    correo = forms.EmailField(required=True)
    ruc = forms.CharField(max_length=13, required=True)
    direccion = forms.CharField(max_length=50, required=True)
    mensaje = forms.CharField(widget=forms.Textarea, required=True)
    aceptar_condiciones = forms.BooleanField(required=True, label='Cuenta con tienda física o en línea')