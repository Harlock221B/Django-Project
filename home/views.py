from django.db.models.query_utils import Q
from django.shortcuts import render, Http404, get_object_or_404, redirect
from .models import Curso
from django.contrib import messages



def index(request):
    dados = Curso.objects.order_by('-id').filter(
        mostrar=True
    )
    return render(request, 'home/index.html', {'dados': dados})


def mostrar(request, idbusca):
    dados = get_object_or_404(Curso, id=idbusca)
    return render(request, 'home/detcurso.html', {'dados': dados})


def buscar(request):
    x = request.GET['buscar']
    
    if x is None or not x:
        messages.add_message(request, messages.INFO,'Digite um valor valido')
        redirect('home')
    
    dados = Curso.objects.order_by('titulo').filter(
        Q(titulo__icontains=x) | Q(descricao__icontains=x)
    )
    return render(request, 'home/index.html', {'dados': dados})
