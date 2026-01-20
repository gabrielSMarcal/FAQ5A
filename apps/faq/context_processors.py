from .models import Topico

def menu_topicos(request):
    if request.user.is_authenticated:
        topicos = Topico.objects.filter(usuario=request.user).order_by('titulo')
    else:
        topicos = []
    
    return {
        'topicos_menu': topicos
    }
