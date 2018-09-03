# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.urls import include, path
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

from . import views as forca

app_name = 'forca'

urlpatterns = [
    path('perfil/', forca.Perfil.as_view(), name='perfil'),
    path('ranking/', forca.Ranking.as_view(), name='ranking'),
    path('jogo/', forca.Jogo.as_view(), name='jogo'),
    path('palavra/cadastro/', forca.Palavra.as_view(), name='palavra'),
]