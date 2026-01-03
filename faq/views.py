from django.shortcuts import render

def index(request):
    return render(request, 'faq/index.html')

def adicionar(request):
    if request.method == 'POST':
        # Lógica para processar o formulário de adição de FAQ
        pass
    return render(request, 'faq/adicionar.html')
