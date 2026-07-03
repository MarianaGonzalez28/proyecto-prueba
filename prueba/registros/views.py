from django.shortcuts import render
from .models import Alumnos, ComentarioContacto
# Accedemos al modelo Alumnos que contine la esctructura de la tabla
from .forms import ComentarioContactoForm

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