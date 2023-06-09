from django.shortcuts import render, redirect
from .forms import ContactForm
# Create your views here.


def Contact(request):
    contact_form = ContactForm()

    if request.method=="POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            nombres=request.POST.get("nombres")
            correo=request.POST.get("correo")
            ruc=request.POST.get("Ruc")
            direccion= request.POST.get("Direccion")
            mensaje=request.POST.get("Mensaje")
            aceptar_condiciones= request.POST.get(label="aceptar_condiciones")
        
            return redirect("/contacto/?valido")
        

    return render(request, "contact/contact.html", {'form':contact_form})
