from django import forms
from django.forms import inlineformset_factory
from .models import Topico, Citacao

class TopicoForm(forms.ModelForm):
    class Meta:
        model = Topico
        fields = ['titulo', 'descricao']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'placeholder': 'Ex: Atraso na Entrega', 
                'required': True,
                'class': 'form-input'
            }),
            'descricao': forms.Textarea(attrs={
                'rows': '8', 
                'placeholder': 'Descreva o assunto detalhadamente...', 
                'required': True,
                'class': 'form-input'
            }),
        }

class CitacaoForm(forms.ModelForm):
    class Meta:
        model = Citacao
        fields = ['texto']
        widgets = {
            'texto': forms.TextInput(attrs={
                'placeholder': 'Digite a citação aqui...',
                'class': 'form-input'
            }),
        }

    def clean_texto(self):
        texto = self.cleaned_data.get('texto')
        if texto and "\n" in texto:
            raise forms.ValidationError("A citação não pode conter quebras de linha.")
        return texto

# Criar o FormSet para Citações vinculadas ao Tópico
CitacaoFormSet = inlineformset_factory(
    Topico, 
    Citacao, 
    form=CitacaoForm,
    extra=1,      # Começa com 1 campo vazio
    can_delete=True
)
