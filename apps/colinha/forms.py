from django import forms
from .models import Colinha

class ColinhaForm(forms.ModelForm):
    class Meta:
        model = Colinha
        fields = ['titulo', 'conteudo']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'placeholder': 'Ex: Saudação Inicial',
                'class': 'form-input',
                'required': True
            }),
            'conteudo': forms.Textarea(attrs={
                'placeholder': 'Digite o texto da colinha aqui...',
                'class': 'form-input',
                'rows': '4',
                'required': True
            }),
        }
