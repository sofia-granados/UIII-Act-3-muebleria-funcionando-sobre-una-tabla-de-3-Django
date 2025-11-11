from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    
    # URLs para Empleados
    path('empleados/', views.inicio_empleados, name='ver_empleados'),
    path('empleados/agregar/', views.agregar_empleado, name='agregar_empleado'),
    path('empleados/actualizar/', views.actualizar_empleados, name='actualizar_empleados'),
    path('empleados/actualizar/<int:id_empleado>/', views.realizar_actualizacion_empleados, name='realizar_actualizacion'),
    path('empleados/borrar/<int:id_empleado>/', views.borrar_empleados, name='borrar_empleado'),
]