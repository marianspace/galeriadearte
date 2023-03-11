from re import I
from django.shortcuts import render
from django.contrib.auth import login as Login, authenticate
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from .form import *
from .models import *

# Create your views here.

# Vistas paginas 
def inicio(request): 
    if request.user.is_authenticated:
        return render(request, "agalery/index.html",{'user_avatar':buscar_url_avatar(request.user)}) 
    else:
        return render(request, "agalery/index.html")
   
def obras(request):
     return render(request, 'agalery\obra.html')
    
def buscarobras(request):
     query = request.GET.get('titulo')
     if query is not None:
         resultados = obra.objects.filter(titulo__icontains=query)
     else:
         resultados = []
     return render(request, 'agalery/buscar_obra.html', {'resultados': resultados})
    
def todas_obras(request):
      obras = obra.objects.all()
      return render(request, 'agalery/obra.html', {'obras': obras})   
    
def nosotros(request): 
    return render (request,'agalery/nosotros.html')

def perfil(request):
    mas_datos, _ = usuario_a.objects.get_or_create(user=request.user)
    return render(request, "agalery/perfil_user.html", {'mas_datos':mas_datos ,'user_avatar':buscar_url_avatar(request.user)})

def buscar_url_avatar(user):
    usuario_extendido, _ = usuario_a.objects.get_or_create(user=user)
    if usuario_extendido.imagen:
        return usuario_extendido.imagen.url
    else:
        return 'https://www.gravatar.com/avatar/' 

# Login Registro

def register (request): 
    if request.method == 'POST':
        form = form_register(request.POST,request.FILES)
        if form.is_valid():    
            username = form.cleaned_data['username']
            form.save()
            return render(request, "agalery/index.html", {'msj':f'Se creo el user {username}'})
        else:
            return render(request, "agalery/register.html", {'form':form})
    form = form_register()
    return render(request, "agalery/register.html", {'form':form})

def login (request): 
    if request.method == 'POST':  
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not  None:
                Login(request, user)
                usuario = form.cleaned_data['username']
                return render(request, "agalery/index.html", {'msj':f'Bienvenido {usuario}!', 'user_avatar':buscar_url_avatar(request.user)})
            else:
                return render(request, 'agalery/login.html', {'form':form})
        else:
            return render(request, 'agalery/login.html', {'form':form})
    else:
        form = AuthenticationForm()
        return render(request, 'agalery/login.html', {'form':form})

@login_required
def editar (request):
    usuario_extendido, _ = usuario_a.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = form_edit_user(request.POST,request.FILES)
        if form.is_valid():           
            data = form.cleaned_data
            logued_user = request.user 
            logued_user.email = data.get('email')
            logued_user.first_name = data.get('first_name',)
            logued_user.last_name = data.get('last_name')
            usuario_extendido.imagen = data['imagen']
            usuario_extendido.link= data['link']
            usuario_extendido.bio = data['bio']
            if data.get('password1') == data.get('password2') and len(data.get("password1")) >8:
                logued_user.set_password(data.get('password1'))
                msj = 'Se actualizo la contraseña' 
            else:
                msj = 'Se actualizo el perfil'
            logued_user.save()
            usuario_extendido.save()          
            return render(request, "agalery/index.html", {'msj':msj, 'user_avatar':buscar_url_avatar(request.user)})
        else:
            return render(request, "agalery/index.html", {'form':form, 'msj':'', 'user_avatar':buscar_url_avatar(request.user)})      
    form = form_edit_user(
        initial={
            'email': request.user.email,
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'imagen': usuario_extendido.imagen,
            'link': usuario_extendido.link,
            'bio': usuario_extendido.bio
        }
    )
    return render(request, "agalery/editar_user.html", {'form':form, 'msj':'', 'user_avatar':buscar_url_avatar(request.user)})

# Registro de obra
@login_required
def registrar_obra(request):
     form = registro_obra()
     if request.method == 'POST':
         form = registro_obra(request.POST)
         if form.is_valid():
             #first_name = form.cleaned_data['Nombre']
             #last_name = form.cleaned_data['Apellido']
             titulo = form.cleaned_data['titulo']
             descripcion = form.cleaned_data['descripcion']
             precio = form.cleaned_data['precio']
             obra_nueva = obra(titulo=titulo, descripcion=descripcion, precio=precio)
             obra_nueva.save()
             msj = 'Obra agregada'
             return render(request, 'agalery/index.html', {'msj':'Obra agregada'})
     return render(request, 'agalery/registro_obra.html', {'form': form, 'registro_obra': registro_obra})   
    
@login_required
def editar_obra (request):
    usuario_obra, _ = registro_obra.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        formobra = form_edit_obra(request.POST,request.FILES)
        if formobra.is_valid():           
            data = formobra.cleaned_data
            logued_user = request.user 
            logued_user.email = data.get('email')
            usuario_obra.titulo = data['titulo']
            usuario_obra.descripcion= data['descripción']
            usuario_obra.imagen = data['imagen']
            usuario_obra.precio = data['precio']
            # if data.get('password1') == data.get('password2') and len(data.get("password1")) >8:
            #     logued_user.set_password(data.get('password1'))
            #     msj = 'Se actualizo la contraseña' 
            # else:
            msj = 'Se realizaron cambios'
            logued_user.save()
            usuario_obra.save()          
            return render(request, "agalery/index.html", {'msj':msj, 'user_avatar':buscar_url_avatar(request.user)})
        else:
            return render(request, "agalery/index.html", {'form':form, 'msj':'', 'user_avatar':buscar_url_avatar(request.user)})      
    form = form_edit_obra(
        initial={
            'email': request.user.email,
            'titulo': usuario_obra.titulo,
            'descripcion': usuario_obra.descripcion,
            'imagen': usuario_obra.imagen,
            'precio': usuario_obra.precio 
        }
    )
    return render(request, "agalery/editar_obra.html", {'form':form, 'msj':'', 'user_avatar':buscar_url_avatar(request.user)})

def editobra(request):
    mas_datos, _ = obra.objects.get_or_create(user=request.user)
    return render(request, "agalery/perfil_obra.html", {'mas_datos':mas_datos})
