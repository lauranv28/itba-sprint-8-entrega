from django.shortcuts import render

# Create your views here.
def atencion_clientes(request):
    return render(request, 'paginas/atencion_cliente.html')

def home(request):
    return render(request, 'paginas/home.html')

def beneficios(request):
    return render(request, 'paginas/beneficios.html')

def preguntas_frecuentes(request):
    return render(request, 'paginas/preguntas_frecuentes.html')

def turnos(request):
    return render(request, 'paginas/turnos.html')