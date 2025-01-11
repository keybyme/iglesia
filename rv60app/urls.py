
from django.urls import path

from . import views

urlpatterns = [
    
  path('', views.home, name="index"),  
  
  path('dashboard', views.dashboard, name="dashboard"),
 
  path('rvlectura', views.rvlectura, name="rvlectura"),
  
  path('biblia', views.biblia, name="biblia"),
  
  path('doctrina', views.doctrina, name="doctrina"),
  
  path('diccionario', views.diccionario, name="diccionario"),
  
  path('tema', views.tema, name="tema"),
  
 
]