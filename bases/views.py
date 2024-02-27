from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import AnonymousUser

from django.views.generic import *


def is_ajax(request):
    return request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest"


class FormInvalidMixin:
    def form_invalid(self, form):
        response = super().form_invalid(form)
        if is_ajax(request=self.request):
            return JsonResponse(form.errors, status=400)
        return response


class LoginAndPermissionRequiredMixin(
    LoginRequiredMixin, PermissionRequiredMixin, FormInvalidMixin
):
    login_url = "users:login_alt"
    raise_exception = False
    redirect_field_name = "redirect_to"

    def handle_no_permission(self):
        if self.request.user != AnonymousUser():
            self.login_url = "pages:forbidden"
        return HttpResponseRedirect(reverse_lazy(self.login_url))


class CreateOrModifyMixin:
    def form_valid(self, form):
        if form.instance.id:
            form.instance.modified_by = self.request.user
        else:
            form.instance.created_by = self.request.user
        return super().form_valid(form)


# Vista basada en funciones
def first_view(request):
    return HttpResponse("<b>Hola mundo</b> desde el curso de Django")


class HomeView(TemplateView):
    template_name = "bases/home.html"
