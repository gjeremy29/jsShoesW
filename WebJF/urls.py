from django.urls import path

from WebJF import views

urlpatterns = [
    path('',views.home, name="Home"),
    path('vizzano',views.vizzano, name="Vizzano"),
    path('modare',views.modare, name="Modare"),
    path('actvitta',views.actvitta, name="Actvitta"),
    path('brsport',views.brsport, name="Brsport"),
    path('contacto',views.contacto, name="Contacto"),
]