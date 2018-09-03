from django import forms

from . import models

class RegistrationUserForm(forms.ModelForm):
  
  class Meta:
    model = models.UUIDUser
    fields = ('username', 'first_name','email', 'password')
    labels = {
    	'username': 'Nome de Usuário',
        'first_name': 'Nome',
    	'email': 'E-mail',
    	'password': 'Senha',
    }
    widgets = {
      'password': forms.PasswordInput()
    }