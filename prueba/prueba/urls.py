"""
URL configuration for prueba project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inicio import views
from django.conf import settings 
# Permite acceder a las variables MEDIA_URL y MEDIA_ROOT que almacena la ubicacion de nuestras imagenes
from registros import views as views_registros
# Importamos la nueva vista de app registros para poder asignar las rutas de acceso a sus vistas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views_registros.registros, name='Principal'),
    # Indicamos que ahora la ruta de principal.html se encuentra en la view de registros
    #path('', views.principal, name='Principal'),
    path('contacto/', views_registros.contacto, name='Contacto'),
    path('formulario/', views.formulario, name='Formulario'),
    path('ejemplo/', views.ejemplo, name='Ejemplo'),
    path('registrar/', views_registros.registrar, name='Registrar'),
    path('consultaContacto/', views_registros.consultaContacto, name='consultaContacto'),
    path('eliminarComentario/<int:id>/', views_registros.eliminarComentario, name='eliminar'),
    path('editarComentario/<int:id>/', views_registros.editarComentario, name='editar'),
    path('editarComentario/<int:id>/', views_registros.ConsultaComentarioIndividual, name='consulta_individual'),
    path('consultas/', views_registros.registros, name='consultas'),
    path('consultas1/', views_registros.consultar1, name='Consultas'),
    path('consultas2/', views_registros.consultar2, name='Consultas2'),
    path('consultas3/', views_registros.consultar3, name='Consultas3'),
    path('consultas4/', views_registros.consultar4, name='Consultas4'),
    path('consultas5/', views_registros.consultar5, name='Consultas5'),
    path('consultas6/', views_registros.consultar6, name='Consultas6'),
    path('consultas7/', views_registros.consultar7, name='Consultas7'),
    path('consultas8/', views_registros.consultar8, name='Consultas8'),
    path('consultasSQL/', views_registros.consultasSQL, name='sql'),
    path('comentarioContactoPorFecha/', views_registros.comentarioContactoPorFecha, name='Fecha'),
    path('comentarioContactoExpresion/', views_registros.comentarioContactoExpresion, name='Expresion'),
    path('comentarioContactoUsuario/', views_registros.comentarioContactoUsuario, name='Usuario'),
    path('comentarioContacto1/', views_registros.comentarioContacto1, name='Comentario1'),
    path('comentarioContacto2/', views_registros.comentarioContacto2, name='Comentario2'),
    path('comentarioContactoPorFechaSQL/', views_registros.comentarioContactoPorFechaSQL, name='FechaSQL'),
    path('comentarioContactoExpresionSQL/', views_registros.comentarioContactoExpresionSQL, name='ExpresionSQL'),
    path('comentarioContactoUsuarioSQL/', views_registros.comentarioContactoUsuarioSQL, name='UsuarioSQL'),
    path('comentarioContacto1SQL/', views_registros.comentarioContacto1SQL, name='Comentario1SQL'),
    path('comentarioContacto2SQL/', views_registros.comentarioContacto2SQL, name='Comentario2SQL'),
    path('subir', views_registros.archivos, name='Subir'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


