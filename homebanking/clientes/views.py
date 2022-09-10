from http.client import HTTPResponse
from django.shortcuts import render
from .models import Cliente
from django.template import Template, Context

def clientes(request):
    client = Cliente.objects.all()
    return render(request,"clientes/clientes.html", {'client':client})