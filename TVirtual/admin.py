from django.contrib import admin
from .models import Empresa, Cliente, Empleado, Stock, DetallePedido, Pedido, Carrito, UserProfile
# Register your models here.

admin.site.register(UserProfile)

class AdminEmpresa(admin.ModelAdmin):
	list_display = ["__str__","nombre","siglas"]
	list_editable = ["nombre","siglas"]
	list_filter = ["nombre"]
	search_fields = ["nombre","siglas"]

	class Meta:
		model = Empresa
admin.site.register(Empresa,AdminEmpresa)

class AdminEmpleado(admin.ModelAdmin):
	list_display = ["__str__","ci","contraseña","nombre","direccion","email","telefono"]
	list_editable = ["direccion","email","telefono"]
	list_filter = ["ci","contraseña","nombre","direccion","email","telefono"]
	search_fields = ["ci"]

	class Meta:
		model = Empleado
admin.site.register(Empleado,AdminEmpleado)

class AdminCliente(admin.ModelAdmin):
	list_display = ["__str__","ci","contraseña","nombres","apellidos","direccion","email","telefono"]
	list_editable = ["direccion","email","telefono"]
	list_filter = ["ci","contraseña","nombres","apellidos","direccion","email","telefono"]
	search_fields = ["ci"]

	class Meta:
		model = Cliente
admin.site.register(Cliente,AdminCliente)

class AdminStock(admin.ModelAdmin):
	list_display = ["__str__","codigo","nombre","imagen","descripcion","precio","public_date","status"]
	list_editable = ["nombre","imagen","descripcion","precio","status"]
	list_filter = ["codigo","nombre","imagen","descripcion","precio","public_date"]
	search_fields = ["codigo"]

	class Meta:
		model = Stock
admin.site.register(Stock,AdminStock)
