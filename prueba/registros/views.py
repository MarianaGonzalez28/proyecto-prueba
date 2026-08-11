
import datetime
from django.shortcuts import render
from .models import Alumnos, ComentarioContacto, Archivos
# Accedemos al modelo Alumnos que contine la esctructura de la tabla
from .forms import ComentarioContactoForm, FormArchivos
from django.shortcuts import get_object_or_404
from django.contrib import messages


# Create your views here.
def registros(request):
    alumnos = Alumnos.objects.all()
    # all recuper todos los objetos del modelo (registros de la tabla alumnos)
    return render(request, "registros/principal.html", {"alumnos": alumnos})
# Indicamos el lugar donde se renderizará el resultado de la vista
# y enviamos la lista de alumnos recuperados

def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid(): #Si los datos que recibe son correctos
            form.save() #inserta
            comentarios=ComentarioContacto.objects.all()
            return render(request,'registros/consultaContacto.html',{'comentarios':comentarios})
        form = ComentarioContactoForm()
        #Si sale mal se reenvia al formulario los datos ingresados
        return render(request,'registros/contacto.html', {'form': form})
    
def contacto(request):
    return render(request, "registros/contacto.html")

def consultaContacto(request):
    comentarios = ComentarioContacto.objects.all()
    return render(request, "registros/consultaContacto.html", {"comentarios": comentarios})

def eliminarComentario(request, id, confirmacion ='registros/confirmarEliminacion.html'):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    if request.method == 'POST':
        comentario.delete()
        comentarios = ComentarioContacto.objects.all()
        return render(request, 'registros/consultaContacto.html', {'comentarios': comentarios})
    return render(request, confirmacion, {'object': comentario})

def editarComentario(request, id):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    form =  ComentarioContactoForm(request.POST or None, instance=comentario)
    if form.is_valid():
        form.save() #Si el regitro ya existe, se modifica
        comentarios=ComentarioContacto.objects.all()
        return render(request, "registros/consultaContacto.html", {'comentarios': comentarios})
    return render(request, 'registros/editarComentario.html', {'comentario': comentario})

def ConsultaComentarioIndividual(request, id):
    comentario = ComentarioContacto.objects.get(id=id)
    return render(request, 'registros/editarComentario.html', {'comentario': comentario})

#filter nos retornara los registros que coincidan con los parámetros de busqueda de datos
def consultar1(request):
    #con una sola condicion
    alumnos = Alumnos.objects.filter(carrera="TI")
    return render(request, "registros/consultas.html", {"alumnos": alumnos})

def consultar2(request):
    #con una sola condicion
    alumnos = Alumnos.objects.filter(carrera="TI").filter(turno="Matutino")
    return render(request, "registros/consultas.html", {"alumnos": alumnos})

def consultar3(request):
    #si solo deseamos recuperar ciertos datos agregamos la funcion only listando campos que queremos obtenerde
    #la consulta emplear filter o en el ejemplo all
    alumnos = Alumnos.objects.all().only("matricula", "nombre", "carrera", "turno", "imagen")
    return render(request, "registros/consultas.html", {"alumnos": alumnos})

def consultar4 (request):
    # Recupera alumnos con el nombre "juan"
    alumnos = Alumnos.objects.filter(nombre__icontains="juan")
    return render(request, "registros/consultas.html", {"alumnos": alumnos})

def consultar5 (request):
    # Alumnos registrados en el año 2026
    alumnos = Alumnos.objects.filter(created__year=2026)
    return render(request, "registros/consultas.html", {"alumnos": alumnos})

def consultar6 (request):
    alumnos = Alumnos.objects.filter(nombre__in=["Juan","Ana"])
    return render(request, "registros/consultas.html", {"alumnos": alumnos})

def consultar7 (request):
    fechaInicio = datetime.date(2026, 8, 1)
    fechaFin = datetime.date(2026, 8, 30)
    alumnos = Alumnos.objects.filter(created__range=(fechaInicio, fechaFin))
    return render(request, "registros/consultas.html", {"alumnos": alumnos})

def consultar8 (request):
    #Consultando entre modelos
    alumnos = Alumnos.objects.filter(comentario__coment__contains='No Inscrito')
    return render(request, "registros/consultas.html", {"alumnos": alumnos})

def consultasSQL(request):
    alumnos = Alumnos.objects.raw('SELECT id, matricula, nombre, carrera, turno, created FROM registros_alumnos WHERE carrera="TI" ORDER BY turno DESC')
    return render(request, "registros/consultas.html", {"alumnos": alumnos})

# Expresiones ORM
def comentarioContactoPorFecha(request):
    fecha_inicio = datetime.date(2026, 6, 20)
    fecha_fin = datetime.date(2026, 8, 4)
    comentarios = ComentarioContacto.objects.filter(created__range=(fecha_inicio, fecha_fin))
    return render(request, "registros/consultaContacto.html", {"comentarios": comentarios})

def comentarioContactoExpresion(request):
    comentarios = ComentarioContacto.objects.filter(mensaje__icontains="Hola")
    return render(request, "registros/consultaContacto.html", {"comentarios": comentarios})

def comentarioContactoUsuario(request):
    comentarios = ComentarioContacto.objects.filter(usuario__icontains="Mariana")
    return render(request, "registros/consultaContacto.html", {"comentarios": comentarios})

# Comienza con una palabra específica, en este ejemplo "No"
def comentarioContacto1(request):
    comentarios = ComentarioContacto.objects.filter(mensaje__istartswith="No")
    return render(request, "registros/consultaContacto.html", {"comentarios": comentarios})

# Terminan con una palabra específica, en este ejemplo "editado"
def comentarioContacto2(request):
    comentarios = ComentarioContacto.objects.filter(mensaje__iendswith="editado")
    return render(request, "registros/consultaContacto.html", {"comentarios": comentarios})

# Consultas SQL
def comentarioContactoPorFechaSQL(request):
    comentarios = ComentarioContacto.objects.raw('SELECT id, usuario, mensaje, created FROM registros_comentariocontacto WHERE created BETWEEN "2026-06-20 00:00:00" AND "2026-08-04 23:59:59"')
    return render(request, "registros/consultaContacto.html", {"comentarios": comentarios})

def comentarioContactoExpresionSQL(request):
    comentarios = ComentarioContacto.objects.raw('SELECT id, usuario, mensaje, created FROM registros_comentariocontacto WHERE mensaje LIKE "%Hola%"')
    return render(request, "registros/consultaContacto.html", {"comentarios": comentarios})

def comentarioContactoUsuarioSQL(request):
    comentarios = ComentarioContacto.objects.raw('SELECT id, usuario, mensaje, created FROM registros_comentariocontacto WHERE usuario="Mariana"')
    return render(request, "registros/consultaContacto.html", {"comentarios": comentarios})


def comentarioContacto1SQL(request):
    comentarios = ComentarioContacto.objects.raw('SELECT id, usuario, mensaje, created FROM registros_comentariocontacto WHERE mensaje LIKE "No%"')
    return render(request, "registros/consultaContacto.html", {"comentarios": comentarios})

def comentarioContacto2SQL(request):
    comentarios = ComentarioContacto.objects.raw('SELECT id, usuario, mensaje, created FROM registros_comentariocontacto WHERE mensaje LIKE "%editado"')
    return render(request, "registros/consultaContacto.html", {"comentarios": comentarios})

def archivos(request):
    if request.method == 'POST':
        form = FormArchivos(request.POST, request.FILES)
        if form.is_valid():
            titulo = request.POST['titulo']
            descripcion = request.POST['descripcion']
            archivo = request.FILES['archivo']
            insert = Archivos(titulo=titulo, descripcion=descripcion, archivo=archivo)
            insert.save()
            return render(request, "registros/archivos.html")
        else:
            messages.error(request, "Error al procesar formulario")
    else:
        return render(request, "registros/archivos.html", {'archivo':Archivos})