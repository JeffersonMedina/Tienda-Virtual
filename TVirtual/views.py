from django.shortcuts import redirect, render, render_to_response
from .models import Empresa, Empleado, Cliente, Stock, UserProfile
from .forms import FormularioEmpleado, FormularioCliente, FormularioStock, FormularioLogin

from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
#vistas genericas
from django.views.generic import ListView, DetailView, TemplateView
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic.edit import UpdateView, CreateView, DeleteView
#login
from django.template import RequestContext
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
#registro
from django.contrib.auth.models import User
# Create your views here.

def wsProductos(request):
    data = serializers.serialize("json", Stock.objects.filter(status=True)) 
    return HttpResponse(data,content_type='application/json')

def list(request):
    query = Stock.objects.all()
    query = serializers.serialize('json',query)
    return HttpResponse(query, 'application/json')

def registrar(request):
    if request.method == 'POST':
        r = FormularioCliente(request.POST, request.FILES)
        if r.is_valid():
        	datos = r.cleaned_data
        	ci = datos.get('ci')
        	nombres = datos.get('nombres')
        	apellidos = datos.get('apellidos')
        	username = datos.get('username')
        	password = datos.get('password')
        	direccion = datos.get('direccion')
        	email = datos.get('email')
        	telefono = datos.get('telefono')
        	photo = datos.get('photo')
        	# Instanciamos un objeto User, con el username y password
        	user_model = User.objects.create_user(username=username, password=password)
        	# Añadimos datos personales
        	user_model.first_name = nombres
        	user_model.last_name = apellidos
        	user_model.email = email
        	# Y guardamos el objeto, esto guardara los datos en la db.
        	user_model.save()
        	# Ahora, creamos un objeto UserProfile, aunque no haya incluido
        	# una imagen, ya quedara la referencia creada en la db.
        	user_profile = UserProfile()
        	# Al campo user le asignamos el objeto user_model
        	user_profile.user = user_model
        	# y le asignamos la photo (el campo, permite datos null)
        	user_profile.photo = photo
        	# Por ultimo, guardamos tambien el objeto UserProfile
        	user_profile.save()
        	# Ahora, redireccionamos a la pagina gracias.html
        	# Pero lo hacemos con un redirect.
        	return redirect(reverse("Gracias", kwargs={'username':username}))

    else:
        r = FormularioCliente()
    context = {
        'r': r,
    }
    return render(request, "registrar.html", context)

def gracias(request, username):
    return render(request, "gracias.html", {'username': username})

def usuario(request):
	if request.user.is_authenticated():
		return redirect(reverse("Inicio"))

	mensaje = None
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return redirect(reverse("Inicio"))
			else:
				mensaje = "Tu usuario esta inactivo"
		#else:
		mensaje = "Nombre de Usuario y/o Contraseña incorrecto"
	return render(request, "login.html", {"mensaje":mensaje})

def salir(request):
	logout(request)
	return redirect('Inicio')
	
class FotoListView(ListView):
	model = Stock
	template_name ='foto_list.html'

class ActualizarFoto(UpdateView):
	model = Stock
	fields = ['idC','nombre','imagen','descripcion', 'precio']
	template_name_suffix = '_form'

class CrearFoto(CreateView):
	model = Stock
	fields = ['idC','nombre','imagen','descripcion', 'precio']
	template_name_suffix = '_form'

class EliminarFoto(DeleteView):
	model = Stock
	success_url = reverse_lazy('Inicio')
	template_name_suffix = '_delete'