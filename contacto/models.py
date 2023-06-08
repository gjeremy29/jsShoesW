from django.db import models

# Create your models here.

options = [
[0, 'Quito'],
[1, 'Guayaquil'],
[2, 'Cuenca'],
[3, 'Santo Domingo de los Colorados'],
[4, 'Machala'],
[5, 'Manta'],
[6, 'Portoviejo'],
[7, 'Loja'],
[8, 'Ambato'],
[9, 'Esmeraldas'],
[10, 'Durán'],
[11, 'Riobamba'],
[12, 'Quevedo'],
[13, 'Ibarra'],
[14, 'Milagro'],
[15, 'Babahoyo'],
[16, 'Sangolquí'],
[17, 'Latacunga'],
[18, 'Santa Elena'],
[19, 'La Libertad'],
[20, 'Salinas'],
[21, 'Zamora'],
[22, 'Tulcán'],
[23, 'Azogues'],
[24, 'Machachi'],
[25, 'Otavalo'],
[26, 'Vinces'],
[27, 'Nueva Loja'],
[28, 'Chone'],
[29, 'Santa Rosa'],
[30, 'Tena'],
[31, 'Huaquillas'],
[32, 'Playas'],
[33, 'Pasaje'],
[34, 'La Troncal'],
[35, 'Santa Ana'],
[36, 'Puyo'],
[37, 'Jipijapa'],
[38, 'Atuntaqui'],
[39, 'Naranjal'],
[40, 'El Carmen'],
[41, 'Pedro Carbo'],
[42, 'Ventanas'],
[43, 'Sucre'],
[44, 'Pelileo'],
[45, 'Balzar'],
[46, 'San Gabriel'],
[47, 'Santo Domingo'],
[48, 'Ibarra'],
[49, 'Esmeraldas'],
[50, 'Machachi'],
[50, 'Otro']
]

class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name= 'Nombres y Apellidos')
    email = models.EmailField(verbose_name='Correo electrónico')
    contact_type = models.IntegerField(choices=options, verbose_name='Ciudad')
    ruc = models.CharField(max_length=10)
    direccion = models.CharField(max_length=50, unique=True, verbose_name='Dirección de la tienda o nombre en redes sociales')
    message = models.TextField(verbose_name='Mensaje')
    subscription = models.BooleanField(default=False, verbose_name='Tengo tienda física u online ya establecida')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de envío')


