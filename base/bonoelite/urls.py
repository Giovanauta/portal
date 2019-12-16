from . import views
from django.urls import path, include


urlpatterns = [
    path('', views.index),
    path('maestro_trabajador', views.maestro_trabajador),
    path('delete/<id>', views.eliminarTrabajador),  # delete method url


]
