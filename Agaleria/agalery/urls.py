from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.inicio, name="index"),
    path('register/', views.register, name="register"),
    path('login/', views.login, name='login'),
    path('editar/perfil/', views.editar, name='editar'),
    path('perfil/', views.perfil, name='perfil'),     
    path('logout/', LogoutView.as_view(template_name="agalery/index.html"), name='logout'),
    path('nosotros/', views.nosotros, name="nosotros"),
    path('blog/',views.blog, name="blog"),
    path('formulario_post/', views.formulario_posteo, name='formulario_post'),
    path('lista_post/', views.lista_post, name='Lista_posts'),
    path(r'^delete_post/(?P<pk>\d+)/$', views.DeletePost.as_view(), name='delete_posts'),
    path(r'^detalle_post/(?P<pk>\d+)/$', views.DetallePost.as_view(), name='detalle_posts'),

]
 