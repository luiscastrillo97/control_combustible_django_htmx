from django.shortcuts import render
from django.http import HttpResponse


# Vista basada en funciones
def first_view(request):
    return HttpResponse("<b>Hola mundo</b> desde el curso de Django")
