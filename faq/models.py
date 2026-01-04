from django.db import models

class Topico(models.Model):
    
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    criado_em = models.DateTimeField("data de criação", auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.titulo
    
class Citacao(models.Model):
    
    texto = models.TextField()
    topico = models.ForeignKey(Topico, on_delete=models.CASCADE, related_name='citacoes', null=True, blank=True)
    
    def __str__(self):
        return self.texto[:20]
    
