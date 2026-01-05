from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Topico
from .forms import TopicoForm, CitacaoFormSet

@login_required
def index(request, topico_id=None):
    if topico_id:
        topico_selecionado = get_object_or_404(
            Topico.objects.prefetch_related('citacoes'),
            id=topico_id,
            usuario=request.user
        )
    else:
        topico_selecionado = Topico.objects.filter(
            usuario=request.user
        ).prefetch_related('citacoes').first()
        
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
            topico = form.save(commit=False)
            topico.usuario = request.user
            topico.save()
            formset.instance = topico
            formset.save()
            messages.success(request, 'Tópico adicionado com sucesso!')
            return redirect('index_com_id', topico_id=topico.id)
    else:
        form = TopicoForm()
        formset = CitacaoFormSet()
    
    return render(request, 'faq/adicionar.html', {
        'form': form,
        'formset': formset
    })
