from django.shortcuts import render
from django.urls import path
from django.views.generic import *


class AboutView(TemplateView):
    template_name = "paginas/about.html"
