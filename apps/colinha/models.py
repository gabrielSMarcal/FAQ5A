from django.db import models
from django.contrib.auth.models import User

class Colinha(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='colinhas')
    favorito = models.BooleanField(default=False)
    ordem = models.IntegerField(default=0)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-favorito', 'ordem', '-criado_em']

    def __str__(self):
        return self.titulo
