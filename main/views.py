from django.http import HttpResponse
from django.shortcuts import render
from .models import Curso

def hompage(request):
    #return HttpResponse("Hola buenas noches")
    return render(request, "main/inicio.html", {"cursos": Curso.objects.all})