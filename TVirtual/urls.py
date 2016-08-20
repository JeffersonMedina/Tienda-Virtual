from django.conf.urls import patterns, url
from django.contrib import admin

from . import views

urlpatterns = patterns('',
	url(r'^$', views.FotoListView.as_view(), name='Inicio'),
	url(r'^crear/$', views.CrearFoto.as_view(), name='Crear'),

	url(r'^(?P<pk>\d+)/actualizar/$', views.ActualizarFoto.as_view(), name='Actualizar'),
	url(r'^(?P<pk>\d+)/eliminar/$', views.EliminarFoto.as_view(), name='Eliminar'),

	url(r'^registrar/$', views.registrar, name='Registrar'),
	url(r'^empleado/$', views.empleado, name='RegEmpleado'),
	url(r'^login/$', views.usuario, name='Login'),
	url(r'^logout/$', views.salir, name='Logout'),

	url(r'^gracias/(?P<username>[\w]+)/$', views.gracias, name='Gracias'),

	
    #url(r'^ws/productos/$', views.wsProductos, name='WSProductos'),
    url(r'^ws/list/$', views.list, name='WSProductos'),
    url(r'^ws/productos/$', views.survey_list, name='WSProductos'),
)