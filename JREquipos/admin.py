from django.contrib import admin

# Register your models here.
from .models import Equipo, CategoriaEquipos


class EquipoAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

class categoriaEquipoAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')    
admin.site.register(Equipo,EquipoAdmin)
admin.site.register(CategoriaEquipos,categoriaEquipoAdmin)