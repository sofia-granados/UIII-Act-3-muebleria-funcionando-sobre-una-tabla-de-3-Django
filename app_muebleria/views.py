from django.shortcuts import render, redirect, get_object_or_404
from .models import Empleado

# Vistas para Empleados
def inicio_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleado/ver_empleado.html', {'empleados': empleados})

def agregar_empleado(request):
    if request.method == 'POST':
        # Crear nuevo empleado con los datos del formulario
        empleado = Empleado(
            fecha_contratacion=request.POST['fecha_contratacion'],
            nombre=request.POST['nombre'],
            edad=request.POST['edad'],
            cargo=request.POST['cargo'],
            telefono=request.POST['telefono'],
            sueldo=request.POST['sueldo']
        )
        empleado.save()
        return redirect('ver_empleados')
    
    return render(request, 'empleado/agregar_empleado.html')

def actualizar_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleado/actualizar_empleado.html', {'empleados': empleados})

def realizar_actualizacion_empleados(request, id_empleado):
    empleado = get_object_or_404(Empleado, id_empleado=id_empleado)
    
    if request.method == 'POST':
        empleado.fecha_contratacion = request.POST['fecha_contratacion']
        empleado.nombre = request.POST['nombre']
        empleado.edad = request.POST['edad']
        empleado.cargo = request.POST['cargo']
        empleado.telefono = request.POST['telefono']
        empleado.sueldo = request.POST['sueldo']
        empleado.save()
        return redirect('ver_empleados')
    
    return render(request, 'empleado/actualizar_empleado.html', {'empleado': empleado})

def borrar_empleados(request, id_empleado):
    empleado = get_object_or_404(Empleado, id_empleado=id_empleado)
    
    if request.method == 'POST':
        empleado.delete()
        return redirect('ver_empleados')
    
    return render(request, 'empleado/borrar_empleado.html', {'empleado': empleado})

# Vista de inicio
def inicio(request):
    return render(request, 'inicio.html')