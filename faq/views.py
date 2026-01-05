from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Topico
from .forms import TopicoForm, CitacaoFormSet

@login_required
def index(request, topico_id=None):
    if topico_id:
        topico_selecionado = Topico.objects.prefetch_related('citacoes').get(id=topico_id)
    else:
        topico_selecionado = Topico.objects.prefetch_related('citacoes').first()
        
    context = {
        'topico': topico_selecionado
    }
    return render(request, 'faq/index.html', context)

@login_required
def adicionar(request):
    if request.method == 'POST':
        form = TopicoForm(request.POST)
        formset = CitacaoFormSet(request.POST)
        
        if form.is_valid() and formset.is_valid():
            topico = form.save()
            formset.instance = topico
            formset.save()
            return redirect('index_com_id', topico_id=topico.id)
    else:
        form = TopicoForm()
        formset = CitacaoFormSet()
    
    return render(request, 'faq/adicionar.html', {
        'form': form,
        'formset': formset
    })
