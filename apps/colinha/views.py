from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
import json

from .models import Colinha
from .forms import ColinhaForm

@login_required
def index(request):
    colinhas_favoritas = Colinha.objects.filter(
        usuario=request.user,
        favorito=True
    ).order_by('ordem', '-criado_em')
    
    colinhas_normais = Colinha.objects.filter(
        usuario=request.user,
        favorito=False
    ).order_by('ordem', '-criado_em')
    
    form = ColinhaForm()
    
    if request.method == 'POST':
        form = ColinhaForm(request.POST)
        if form.is_valid():
            colinha = form.save(commit=False)
            colinha.usuario = request.user
            colinha.save()
            messages.success(request, 'Colinha adicionada com sucesso!')
            return redirect('colinhas')
            
    return render(request, 'colinha/index.html', {
        'colinhas_favoritas': colinhas_favoritas,
        'colinhas_normais': colinhas_normais,
        'form': form
    })

@login_required
def editar(request, pk):
    colinha = get_object_or_404(Colinha, pk=pk, usuario=request.user)
    
    if request.method == 'POST':
        form = ColinhaForm(request.POST, instance=colinha)
        if form.is_valid():
            form.save()
            messages.success(request, 'Colinha atualizada com sucesso!')
            return redirect('colinhas')
    
    return redirect('colinhas')

@login_required
def excluir(request, pk):
    colinha = get_object_or_404(Colinha, pk=pk, usuario=request.user)
    
    if request.method == 'POST':
        colinha.delete()
        messages.success(request, 'Colinha excluída com sucesso!')
        return redirect('colinhas')
    
    return redirect('colinhas')

@login_required
@require_POST
def toggle_favorito(request, pk):
    colinha = get_object_or_404(Colinha, pk=pk, usuario=request.user)
    colinha.favorito = not colinha.favorito
    colinha.save()
    return JsonResponse({'favorito': colinha.favorito})

@login_required
@require_POST
def reordenar(request):
    try:
        data = json.loads(request.body)
        ordem = data.get('ordem', [])
        
        for index, colinha_id in enumerate(ordem):
            Colinha.objects.filter(
                pk=colinha_id,
                usuario=request.user
            ).update(ordem=index)
        
        return JsonResponse({'success': True})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=400)
