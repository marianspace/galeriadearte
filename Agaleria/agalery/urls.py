from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.inicio, name="index"),
    path('obra/', views.todas_obras, name='obra'),
    path('buscar_obras/', views.buscarobras, name='buscarobras'),    
    path('register/', views.register, name="register"),
    path('login/', views.login, name='login'),
    path('editar/perfil/', views.editar, name='editar'),
    path('perfil/', views.perfil, name='perfil'),     
    path('logout/', LogoutView.as_view(template_name="agalery/index.html"), name='logout'),
    path('nosotros/', views.nosotros, name="nosotros"),
    path('registro_obra/', views.registrar_obra, name='registro_obra'),
    path('editar/obra/', views.editar_obra, name='editarobra'),
    path('pobra/', views.editobra, name='pobra'),
] 
 