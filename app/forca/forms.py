from django import forms

from . import models

class PalavraForm(forms.ModelForm):
  
  class Meta:
    model = models.Palavra
    fields = ['palavra']
    labels = {
    	'palavra': 'Palavra',
    }