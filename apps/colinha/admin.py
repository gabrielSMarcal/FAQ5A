from django.contrib import admin

from .models import Colinha

class ListandoColinhas(admin.ModelAdmin):
    list_display = ('id', 'titulo','conteudo')
    list_display_links = ('id', 'titulo')
    search_fields = ('titulo', 'conteudo')
    ordering = ('titulo',)
    list_per_page = 10

admin.site.register(Colinha, ListandoColinhas)