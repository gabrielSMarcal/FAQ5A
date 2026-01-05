from django import forms
import re

class LoginForms(forms.Form):
    nome_login=forms.CharField(
        label='Nome de Login',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: João'
            }
        )
    )
    senha=forms.CharField(
        label='Senha',
        required=True,
        max_length=60,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha'
            }
        )
    )
    
class CadastroForms(forms.Form):
    nome_cadastro=forms.CharField(
        label='Nome completo',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Informe o seu login | Ex.: João Silva'
            }
        )
    )
    email=forms.EmailField(
        label='Email',
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Informe o seu email | Ex.: joao@example.com.br'
            }
        )
    )
    senha_1=forms.CharField(
        label='Senha',
        required=True,
        max_length=60,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha'
            }
        )
    )
    senha_2=forms.CharField(
        label='Confirmação de Senha',
        required=True,
        max_length=60,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha novamente'
            }
        )
    )
    
    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get('nome_cadastro')
        
        if nome:
            nome = nome.strip()
            if ' ' in nome:
                raise forms.ValidationError('Espaços não são permitidos neste campo')
            else:
                return nome
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        
        if email:
            # Padrão regex para validar email
            padrao_email = r'^[a-zA-Z0-9._-]+@([a-z0-9]+)(\.[a-z]{2,3})+$'
            
            if not re.match(padrao_email, email):
                raise forms.ValidationError('Email inválido. Use o formato correto.')
            
            return email
       
    def clean_senha_2(self):
        senha_1 = self.cleaned_data.get('senha_1')
        senha_2 = self.cleaned_data.get('senha_2')
        
        if senha_1 and senha_2:
            if senha_1 != senha_2:
                raise forms.ValidationError('Senhas não coicidem')
            else:
                return senha_2
