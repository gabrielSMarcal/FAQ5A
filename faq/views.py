from django.shortcuts import render
from .models import Topico, Citacao

def index(request, topico_id=None):
    if topico_id:
        topico_selecionado = Topico.objects.prefetch_related('citacoes').get(id=topico_id)
    else:
        topico_selecionado = Topico.objects.prefetch_related('citacoes').first()
        
    context = {
        'topico': topico_selecionado
    }
    return render(request, 'faq/index.html', context)

def adicionar(request):
    if request.method == 'POST':
        # Lógica para processar o formulário de adição de FAQ
        pass
    return render(request, 'faq/adicionar.html')
