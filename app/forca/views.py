from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from . import forms

from . import models

class Perfil (LoginRequiredMixin, TemplateView):
	template_name = 'perfil.html'


class Ranking (TemplateView):
	template_name = 'ranking.html'

class Jogo (TemplateView):
	template_name = 'jogo.html'

class Palavra(LoginRequiredMixin, CreateView):
	template_name = 'cadastroPalavra.html'
	model = models.Palavra
	success_url = reverse_lazy('forca:perfil')
	form_class = forms.PalavraForm

	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.save()
		return super(Palavra, self).form_valid(form)