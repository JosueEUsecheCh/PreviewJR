from django.contrib import admin

# Register your models here.
from .models import CategoriaAudioVideo, ComponenteAudioVideo


class audioVideoAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

class categoriaAudioVideoAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')    
admin.site.register(ComponenteAudioVideo,audioVideoAdmin)
admin.site.register(CategoriaAudioVideo,categoriaAudioVideoAdmin)