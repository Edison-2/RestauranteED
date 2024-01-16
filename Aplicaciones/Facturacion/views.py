from django.shortcuts import render, redirect
from .models import Provincia
from .models import Cliente

from django.contrib import messages
# Create your views here.
def listadoProvincias(request):
    restauramteBdd=Provincia.objects.all()
    return render(request,"listadoProvincias.html",{'provincias':restauramteBdd})
def guardarProvincia(request):
    region_ed = request.POST["region_ed"]
    nombre_ed = request.POST["nombre_ed"]
    capital_ed = request.POST["capital_ed"]
    prefijo_ed = request.POST["prefijo_ed"]

    nuevaProvincia = Provincia.objects.create(region_ed=region_ed, nombre_ed=nombre_ed, capital_ed=capital_ed, prefijo_ed=prefijo_ed)

    messages.success(request, 'Provincia Guardada Exitosamente')
    return redirect('/')
def eliminarProvincia(request, id):
    provinciaEliminar = Provincia.objects.get(id_ed=id)
    provinciaEliminar.delete()
    messages.success(request, 'Provincia Eliminada Exitosamente')
    return redirect('/')

def editarProvincia(request, id):
    provinciaEditar = Provincia.objects.get(id_ed=id)
    return render(request, 'editarProvincia.html', {'provincia': provinciaEditar})


def procesarActualizacionProvincia(request):
    id_ed = request.POST["id"]
    region_ed = request.POST["region_ed"]
    nombre_ed = request.POST["nombre_ed"]
    capital_ed = request.POST["capital_ed"]
    prefijo_ed = request.POST["prefijo_ed"]

    # Obtener la provincia a editar
    provinciaEditar = Provincia.objects.get(id_ed=id_ed)

    # Actualizar los datos de la provincia
    provinciaEditar.region_ed = region_ed
    provinciaEditar.nombre_ed = nombre_ed
    provinciaEditar.capital_ed = capital_ed
    provinciaEditar.prefijo_ed = prefijo_ed

    # Guardar los cambios
    provinciaEditar.save()

    messages.success(request, 'Provincia Actualizada Exitosamente')
    return redirect('/')


def listadoClientes(request):
    clientesBdd = Cliente.objects.all()
    restauramteBdd=Provincia.objects.all()
    return render(request, "listadoClientes.html", {'clientes': clientesBdd, 'provincias':restauramteBdd})

def guardarCliente(request):
    nombre = request.POST["nombre"]
    cedula = request.POST["cedula"]
    correo = request.POST["correo"]
    telefono = request.POST["telefono"]
    provincia_id = request.POST["provincia"]

    # Obtener la provincia seleccionada
    provinciaSeleccionada = Provincia.objects.get(id_ed=provincia_id)

    nuevoCliente = Cliente.objects.create(nombre=nombre, cedula=cedula, correo=correo, telefono=telefono, provincia=provinciaSeleccionada)

    messages.success(request, 'Cliente Guardado Exitosamente')
    return redirect('/')

def eliminarCliente(request, id):
    clienteEliminar = Cliente.objects.get(id=id)
    clienteEliminar.delete()
    messages.success(request, 'Cliente Eliminado Exitosamente')
    return redirect('/')

def editarCliente(request, id):
    clienteEditar = Cliente.objects.get(id=id)
    provinciasBdd = Provincia.objects.all()
    return render(request, 'editarCliente.html', {'cliente': clienteEditar, 'provincias': provinciasBdd})

def procesarActualizacionCliente(request):
    id = request.POST["id"]
    nombre = request.POST["nombre"]
    cedula = request.POST["cedula"]
    correo = request.POST["correo"]
    telefono = request.POST["telefono"]
    provincia_id = request.POST["provincia"]

    # Obtener la provincia seleccionada
    provinciaSeleccionada = Provincia.objects.get(id_ed=provincia_id)

    # Obtener el cliente a editar
    clienteEditar = Cliente.objects.get(id=id)

    # Actualizar los datos del cliente
    clienteEditar.nombre = nombre
    clienteEditar.cedula = cedula
    clienteEditar.correo = correo
    clienteEditar.telefono = telefono
    clienteEditar.provincia = provinciaSeleccionada

    # Guardar los cambios
    clienteEditar.save()

    messages.success(request, 'Cliente Actualizado Exitosamente')
    return redirect('/')
