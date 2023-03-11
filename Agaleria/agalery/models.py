from django.db import models
from datetime import date
from django.contrib.auth.models import User


# Create your models here.

class usuario_a(models.Model):
    imagen = models.ImageField(upload_to='avatares', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.URLField(null=True, blank=True)
    bio = models.TextField(null=True, max_length=150)
    
    def __str__(self):
        return self.user.username
    
class Post(models.Model):
    titulo = models.CharField(max_length=20)
    subtitulo = models.CharField(max_length=50)
    texto = models.TextField(max_length=2000)
    autor = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='imagenes_posts', null=True, blank=True)
    fecha = models.DateField(default=date.today)
    
    def __str__(self):
        return self.titulo