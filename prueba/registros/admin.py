from symtable import Class

from django.contrib import admin
from .models import Alumnos
from .models import Comentario
from .models import ComentarioContacto

# Register your models here.
class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ("created", "updated") #Hace que los campos de fecha y hora no se puedan editar
    list_display = ('matricula','nombre','carrera','turno','created')
    search_fields = ('matricula','nombre','carrera','turno')
    date_hierarchy = 'created'
    list_filter = ('carrera','turno','created')

    list_display_links = ('matricula','nombre') #Para hacer click en la matricula o en el nombre
    list_per_page = 5 #Para poner paginación
    #list_editable = ('turno',) #Editar dentro de la consulta

    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name='usuarios').exists():
            #bloquea los campos
            return ('matricula','carrera', 'turno')
            #Cualquier otro usuario que no sea del grupo Usuarios podra editar los campos
        elif request.user.groups.filter(name='usuario2').exists():
            #bloquea los campos
            return ('matricula', 'turno')
        else:
            #Bloquea los campos
            return ('created', 'updated')
          
admin.site.register(Alumnos, AdministrarModelo)


class AdministrarComentarios(admin.ModelAdmin):
    list_display = ('id','coment')
    search_fields = ('id','created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id') 

    #exclude = ('alumno',) #Para que no se muestre el campo alumno en el formulario de comentarios
admin.site.register(Comentario, AdministrarComentarios)

class AdministrarComentariosContacto(admin.ModelAdmin):
    list_display = ('id', 'mensaje')
    search_fields = ('id','created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')
admin.site.register(ComentarioContacto, AdministrarComentariosContacto)