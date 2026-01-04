from .models import Topico

def menu_topicos(request):
    return {
        'topicos_menu': Topico.objects.all()
    }
