from django.db import models
from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.core.urlresolvers import reverse

# Create your models here.
class Empresa(models.Model):
	nombre = models.CharField(max_length=30)
	siglas = models.CharField(max_length=5)
	logo = models.FilePathField(max_length=20,blank=True,null=True)

	def __str__(self):
		return self.nombre

class Empleado(models.Model):
	idCA = models.ForeignKey(Empresa, on_delete=models.CASCADE,default="")
	ci = models.CharField(max_length=10)
	contraseña = models.CharField(max_length=30)
	nombre = models.CharField(max_length=30)
	direccion = models.TextField(max_length=100)
	email = models.EmailField(max_length=30,blank=True,null=True)
	telefono = models.CharField(max_length=15,blank=True,null=True)

	def __str__(self):
		return self.ci

class Cliente(models.Model):
	idCA = models.ForeignKey(Empresa, on_delete=models.CASCADE,default="")
	ci = models.CharField(max_length=10)
	contraseña = models.CharField(max_length=30)
	nombres = models.CharField(max_length=30)
	apellidos = models.CharField(max_length=30)
	direccion = models.TextField(max_length=100)
	email = models.EmailField(max_length=30,blank=True,null=True)
	telefono = models.CharField(max_length=15,blank=True,null=True)

	def __str__(self):
		return self.ci

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    photo = models.ImageField(upload_to='profiles', blank=True, null=True)
    def __str__(self):
        return self.user.username

class Stock(models.Model):
	idC = models.ForeignKey(Empresa, on_delete=models.CASCADE,default="")
	codigo = models.AutoField(primary_key=True, editable=False)
	nombre = models.CharField(max_length=100)
	imagen = models.ImageField(upload_to='foto/')
	descripcion = models.TextField(max_length=2000)
	precio = models.DecimalField(max_digits=6, decimal_places=2)
	public_date = models.DateField(auto_now_add=True)
	status = models.BooleanField(default=False)

	def __str__(self):
		return self.nombre

	def foto_delete(sender, instance, **kwargs):
		instance.foto.delete(False)

	def get_absolute_url(self):
		return reverse('Inicio')

class DetallePedido(models.Model):
	pedidos = models.AutoField(primary_key=True, editable=False)
	articulo = models.ForeignKey(Stock, on_delete=models.CASCADE, default="")
	cantidad = models.IntegerField()
	total = models.DecimalField(max_digits=6, decimal_places=2)

	def __str__(self):
		return self.pedidos

class Pedido(models.Model):
	pedido = models.ForeignKey(DetallePedido, on_delete=models.CASCADE, default="")
	cliente = models.ManyToManyField(Cliente)
	fecha = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.pedido

class Carrito(models.Model):
	codigo = models.ForeignKey(Stock, on_delete=models.CASCADE, default="")
	cantidad = models.IntegerField()

	def __str__(self):
		return self.codigo

