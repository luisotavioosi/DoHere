# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from DoHere_site import models


class usuarioAdm(admin.ModelAdmin):
	list_display = ['nome', 'tipo']



admin.site.register(models.usuario, usuarioAdm)
admin.site.register(models.pessoa_comum)
admin.site.register(models.aluno)
admin.site.register(models.professor)
admin.site.register(models.tecnico)
admin.site.register(models.pedido)
admin.site.register(models.pacote)
admin.site.register(models.item)
admin.site.register(models.imagem)
admin.site.register(models.endereco)
admin.site.register(models.espaco)
admin.site.register(models.recurso)
admin.site.register(models.servico)
admin.site.register(models.curso)
admin.site.register(models.tecnico_cargo)
admin.site.register(models.usuario_status)
admin.site.register(models.usuario_tipo)