from django.http import HttpResponse
from django.shortcuts import render


def hompage(request):
    return HttpResponse("Hola bunas nochs")
