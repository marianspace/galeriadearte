from django.db import models
from django.db.models import Model
from datetime import date
from django.contrib.auth.models import User


# Create your models here.

class usuario_a(models.Model):
    nombre = models.CharField(max_length=100, help_text="Nombre") 
    apellido = models.CharField(max_length=100, help_text="Apellido")
    imagen = models.ImageField(upload_to='avatares', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.URLField(null=True, blank=True)
    bio = models.TextField(null=True, max_length=150)
    
    def __str__(self):
        return self.user.username
    
class obra(models.Model):
     nombre = models.CharField(max_length=100, help_text="Nombre") 
     apellido = models.CharField(max_length=100, help_text="Apellido")
     titulo = models.CharField(max_length=200, help_text="Titulo de la obra")
     descripcion = models.TextField(max_length=300, help_text="Descripción de la obre en 300 caracteres")
     imagen = models.ImageField(upload_to='imagen', null=True)
     precio = models.IntegerField(default=1) 
     vendida = models.BooleanField(default= False)
    
     def __str__(self):
         return f'{self.titulo}'
     
    
    
    
    
    
    
class Post(models.Model):
    titulo = models.CharField(max_length=20)
    subtitulo = models.CharField(max_length=50)
    texto = models.TextField(max_length=2000)
    autor = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='imagenes_posts', null=True, blank=True)
    fecha = models.DateField(default=date.today)
    
    def __str__(self):
        return self.titulo