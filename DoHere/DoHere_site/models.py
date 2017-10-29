# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class usuario_tipo(models.Model):
    tipo = models.CharField(max_length=50)
    acesso_nivel = models.SmallIntegerField()
    criacao_data = models.DateField(auto_now_add = True)
    modificacao_data = models.DateField(auto_now = True)

class usuario_status(models.Model):
    status = models.CharField(max_length=50)
    criacao_data = models.DateField(auto_now_add = True)
    modificacao_data = models.DateField(auto_now = True)

class tecnico_cargo(models.Model):
    cargo = models.CharField(max_length=50)
    criacao_data = models.DateField(auto_now_add = True)
    modificacao_data = models.DateField(auto_now = True)

class curso(models.Model):
    curso = models.CharField(max_length=30)
    criacao_data = models.DateField(auto_now_add = True)
    modificacao_data = models.DateField(auto_now = True)

class endereco(models.Model):
    lograd = models.CharField(max_length=30)
    numero = models.CharField(max_length=10)
    criacao_data = models.DateField(auto_now_add = True)
    modificacao_data = models.DateField(auto_now = True)

class usuario(models.Model):
    nome = models.CharField(max_length=50)
    nasc_data = models.DateField()
    cpf = models.CharField(max_length=11)
    sexo = models.CharField(max_length=30)
    endereco = models.ForeignKey(endereco, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=11)
    email = models.EmailField()
    senha = models.CharField(max_length=20)
    status = models.ForeignKey(usuario_status, on_delete=models.CASCADE)
    criacao_data = models.DateField(auto_now_add = True)
    modificacao_data = models.DateField(auto_now = True)
    tipo = models.ForeignKey(usuario_tipo, on_delete=models.CASCADE)

class pessoa_comum(models.Model):
    usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
    profissao = models.CharField(max_length=50)

class aluno(models.Model):
    usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
    matricula = models.CharField(max_length=7)
    curso = models.ForeignKey(curso, on_delete=models.CASCADE)

class professor(models.Model):
    usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
    matricula = models.CharField(max_length=7)
    curso = models.ForeignKey(curso, on_delete=models.CASCADE)

class tecnico(models.Model):
    usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
    cargo = models.ForeignKey(tecnico_cargo, on_delete=models.CASCADE)

class item(models.Model):
    item = models.CharField(max_length=50)
    descricao = models.TextField(max_length=1000)
    valor_hora = models.FloatField()
    disponib = models.BooleanField()
    criacao_data = models.DateField(auto_now_add = True)
    modificacao_data = models.DateField(auto_now = True)

class imagem(models.Model):
    item = models.ForeignKey(item)
    imagem_endereco = models.CharField(max_length=500)
    criacao_data = models.DateField(auto_now_add = True)
    modificacao_data = models.DateField(auto_now = True)

class espaco(models.Model):
    item = models.ForeignKey(item)
    area = models.IntegerField() #em metros quadrados
    endereco = models.ForeignKey(endereco)

class recurso(models.Model):
    item = models.ForeignKey(item)
    quantidade = models.IntegerField()

class servico(models.Model):
    item = models.ForeignKey(item)
    responsavel = models.CharField(max_length=50)

class pacote(models.Model):
    item = models.ForeignKey(item)
    criacao_data = models.DateField(auto_now_add = True)
    modificacao_data = models.DateField(auto_now = True)

class pedido(models.Model):
    usuario = models.ForeignKey(usuario)
    pacote = models.ForeignKey(pacote)
    motivo = models.TextField(5000)
    status = models.CharField(max_length=50)
    criacao_data = models.DateField(auto_now_add = True)
    modificacao_data = models.DateField(auto_now = True)

