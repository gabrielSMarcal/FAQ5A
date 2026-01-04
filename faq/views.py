from django.shortcuts import render
from .models import Topico, Citacao

def index(request):
    topicos = Topico.objects.all().prefetch_related('citacoes')
    context = {
        'topicos': topicos
    }
    return render(request, 'faq/index.html', context)

def adicionar(request):
    if request.method == 'POST':
        # Lógica para processar o formulário de adição de FAQ
        pass
    return render(request, 'faq/adicionar.html')
