from django.shortcuts import redirect, render, render_to_response
from .models import Empresa, Stock, UserProfile
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
#rest-frameworl
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SurveySerializer 
# Create your views here.

@api_view(['GET', 'POST'])
def survey_list(request):
    if request.method == 'GET':
        stock = Stock.objects.all()
        serializer = SurveySerializer(stock, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SurveySerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def list(request):
    stock = Stock.objects.all()
    stock = serializers.serialize('json',stock)
    return HttpResponse(stock, 'application/json')

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

def empleado(request):
    if request.method == 'POST':
        r = FormularioEmpleado(request.POST, request.FILES)
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
            user_model.is_staff = True
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
            return redirect(reverse("Inicio"))

    else:
        r = FormularioCliente()
    context = {
        'r': r,
    }
    return render(request, "empleado.html", context)

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