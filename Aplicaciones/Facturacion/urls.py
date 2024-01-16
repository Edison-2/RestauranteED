from django.urls import path
from . import views
urlpatterns=[
path('',views.listadoProvincias),
path('guardarProvincia/',views.guardarProvincia),
path('eliminarProvincia/<id>',views.eliminarProvincia),
path('editarProvincia/<id>',views.editarProvincia),
path ('procesarActualizacionProvincia/', views.procesarActualizacionProvincia),
path('listadoClientes/', views.listadoClientes),
path('guardarCliente/', views.guardarCliente),
path('eliminarCliente/<id>', views.eliminarCliente),
path('editarCliente/<id>', views.editarCliente),
path('procesarActualizacionCliente/', views.procesarActualizacionCliente),

]
