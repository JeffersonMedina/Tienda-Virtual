from django import forms
from .models import  Stock
from django.contrib.auth.models import User

class FormularioEmpleado(forms.Form):
	ci = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}))
	nombres = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
	apellidos = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
	username = forms.CharField(min_length=5, widget=forms.TextInput(attrs={'class': 'form-control'}))
	password = forms.CharField(min_length=5, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
	direccion = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
	telefono = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}))
	photo = forms.ImageField(required=False)

	def clean_username(self):
		username = self.cleaned_data['username']
		if  User.objects.filter(username=username):
			raise forms.ValidationError("Nombre de usuario ya registrado.")
		return username

	def clean_email(self):
		#Comprueba que no exista un email igual
		email = self.cleaned_data['email']
		if User.objects.filter(email=email):
			raise forms.ValidationError("Ya existe un email igual.")
		return email

	def clean_password2(self):
		password = self.cleaned_data['password']
		password2 = self.cleaned_data['password2']
		if password != password2:
			raise forms.ValidationError("La contraseña no coincide.")
		return password2

class FormularioCliente(forms.Form):
	ci = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}))
	nombres = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
	apellidos = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
	username = forms.CharField(min_length=5, widget=forms.TextInput(attrs={'class': 'form-control'}))
	password = forms.CharField(min_length=5, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
	direccion = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
	telefono = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}))
	photo = forms.ImageField(required=False)

	def clean_username(self):
		username = self.cleaned_data['username']
		if  User.objects.filter(username=username):
			raise forms.ValidationError("Nombre de usuario ya registrado.")
		return username

	def clean_email(self):
		#Comprueba que no exista un email igual
		email = self.cleaned_data['email']
		if User.objects.filter(email=email):
			raise forms.ValidationError("Ya existe un email igual.")
		return email

	def clean_password2(self):
		password = self.cleaned_data['password']
		password2 = self.cleaned_data['password2']
		if password != password2:
			raise forms.ValidationError("La contraseña no coincide.")
		return password2

class FormularioStock(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ["nombre","imagen","descripcion","precio"]

class FormularioLogin(forms.Form):
	username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
	password = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={'class': 'form-control'}))


   