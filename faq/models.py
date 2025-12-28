from django.db import models

class Topico(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    criado_em = models.DateTimeField("data de criação", auto_now_add=True)
    
    #Opcional
    citacao = models.TextField(blank=True, null=True)

    @property
    def citacao_lista(self):
        if not self.citacao:
            return []
        return [linha.strip() for linha in self.citacao.splitlines() if linha.strip()]
