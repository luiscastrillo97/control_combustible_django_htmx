from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import *


# Vista basada en funciones
def first_view(request):
    return HttpResponse("<b>Hola mundo</b> desde el curso de Django")


class HomeView(TemplateView):
    template_name = "bases/home.html"
