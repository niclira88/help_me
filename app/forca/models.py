from django.db import models
from app.core.models import UUIDUser 

class Jogo (models.Model):
	usuario = models.ForeignKey(UUIDUser, on_delete = models.CASCADE, related_name = 'usuario', verbose_name = 'Usuário')
	palavra = models.ForeignKey('Palavra', on_delete = models.CASCADE, related_name = 'palavras', verbose_name = 'Palavra')
	status = models.IntegerField (verbose_name = 'Status', default = 0)
	pontuacao = models.IntegerField (verbose_name = 'Pontos')

	def __str__ (self):
		return 'Partida %i %s' % (self.pk, self.user.first_name)

	class Meta:
		verbose_name = 'Partida'
		verbose_name_plural = 'Partidas'

class Palavra (models.Model):
	palavra = models.ForeignKey(UUIDUser, on_delete = models.CASCADE, related_name = 'palavra', verbose_name = 'Palavra')

	def __str__(self):
		return self.palavra

	class Meta:
		verbose_name = 'Palavra'
		verbose_name_plural = 'Palavras'


class Pontuacao (models.Model):
	usuario = models.ForeignKey(UUIDUser, on_delete = models.CASCADE, related_name = 'user', verbose_name = 'Usuário')
	pontuacao = models.IntegerField(verbose_name = 'Pontuação')

	def __str__ (self):
		return 'A pontuação do Usuário: %s, %i pontos'%(self.user.first_name, self.pontuacao)

	class Meta:
		verbose_name = 'Pontuação'
		verbose_name_plural = 'Pontuações'			 