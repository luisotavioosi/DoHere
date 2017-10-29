# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'index.html')

def cadastro(request):
    return render(request, 'cadastro.html')
    
