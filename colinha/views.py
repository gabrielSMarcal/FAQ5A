from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Colinha
from .forms import ColinhaForm

@login_required
def index(request):
    colinhas_list = Colinha.objects.all().order_by('-criado_em')
    form = ColinhaForm()
    
    if request.method == 'POST':
        form = ColinhaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('colinhas')
            
    return render(request, 'colinha/index.html', {
        'colinhas': colinhas_list,
        'form': form
    })

def editar(request, pk):
    colinha = get_object_or_404(Colinha, pk=pk)
    
    if request.method == 'POST':
        form = ColinhaForm(request.POST, instance=colinha)
        if form.is_valid():
            form.save()
            return redirect('colinhas')
    
    return redirect('colinhas')

def excluir(request, pk):
    colinha = get_object_or_404(Colinha, pk=pk)
    
    if request.method == 'POST':
        colinha.delete()
        return redirect('colinhas')
    
    return redirect('colinhas')
