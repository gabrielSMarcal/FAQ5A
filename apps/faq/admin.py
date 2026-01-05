from django.contrib import admin
from .models import Topico, Citacao

class ListandoCitacoes(admin.ModelAdmin):
    list_display = ('id', 'topico','texto')
    list_display_links = ('id', 'topico')
    search_fields = ('texto',)
    ordering = ('topico',)
    list_per_page = 10
    
class ListandoTopicos(admin.ModelAdmin):
    list_display = ('id', 'titulo','criado_em','atualizado_em')
    list_display_links = ('id', 'titulo')
    search_fields = ('titulo', 'descricao')
    ordering = ('titulo',)
    list_per_page = 10
    
admin.site.register(Topico, ListandoTopicos)
admin.site.register(Citacao, ListandoCitacoes)
