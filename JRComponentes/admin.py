from django.contrib import admin

# Register your models here.
from .models import Componentes, categoriaComponentes


class ComponentesAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

class categoriaComponentesAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')    
admin.site.register(Componentes,ComponentesAdmin)
admin.site.register(categoriaComponentes,categoriaComponentesAdmin)