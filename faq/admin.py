from django.contrib import admin
from .models import Topico, Citacao

class ListandoCitacoes(admin.ModelAdmin):
    list_display = ('id', 'topico','texto')
    list_display_links = ('id', 'topico')
    search_fields = ('texto',)
    ordering = ('topico',)
    
admin.site.register(Topico)
admin.site.register(Citacao, ListandoCitacoes)
