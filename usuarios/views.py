from django.shortcuts import render
from django.views.generic import *
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm


class RegisterUserView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("users:login_alt")
    template_name = "usuarios/register.html"
