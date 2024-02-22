from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import *
from .forms import *


class ListBrands(ListView):
    template_name = "ctrl_comb/brand.html"
    model = Brand
    context_object_name = "objects"
    ordering = ["description"]


def save_brand(request):
    context = {}
    template_name = "ctrl_comb/brand-list.html"

    if request.method == "POST":
        id = request.POST.get("id")
        description = request.POST.get("description")
        brand = None

        if id:
            brand = Brand.objects.filter(id=id).first()
        else:
            brand = Brand.objects.filter(description=description).first()

        if brand:
            brand.description = description
            brand.save()
        else:
            brand = Brand.objects.create(description=description)

    objects = Brand.objects.all().order_by("description")
    context["register"] = brand
    context["objects"] = objects

    return render(request, template_name, context)


def delete_brand(request, id):
    context = {}
    template_name = "ctrl_comb/brand-list.html"

    object_to_eliminate = Brand.objects.filter(id=id).first()
    object_to_eliminate.delete()

    objects = Brand.objects.all().order_by("description")
    context["objects"] = objects

    return render(request, template_name, context)


def edit_brand(request, id=None):
    context = {}
    template_name = "ctrl_comb/brand-form.html"

    if id:
        object = Brand.objects.filter(id=id).first()
        form = BrandForm(instance=object)
    else:
        form = BrandForm()

    context["form"] = form
    context["object"] = object

    return render(request, template_name, context)


class ListCarModels(ListView):
    model = CarModel
    template_name = "ctrl_comb/car-model.html"
    context_object_name = "objects"
    ordering = ["brand", "description"]


class CreateCarModel(CreateView):
    model = CarModel
    template_name = "ctrl_comb/car-model-form.html"
    form_class = CarModelForm
    context_object_name = "object"
    success_url = reverse_lazy("control:model_list")


class UpdateCarModel(UpdateView):
    model = CarModel
    template_name = "ctrl_comb/car-model-form.html"
    form_class = CarModelForm
    context_object_name = "object"
    success_url = reverse_lazy("control:model_list")


class DeleteCarModel(DeleteView):
    model = CarModel
    template_name = "bases/delete.html"
    context_object_name = "object"
    success_url = reverse_lazy("control:model_list")


class UpdateCarModelWithModal(UpdateView):
    model = CarModel
    template_name = "ctrl_comb/car-model-edit-modal.html"
    form_class = CarModelForm
    context_object_name = "object"
    success_url = reverse_lazy("control:model_list")


class CreateCarModelWithModal(CreateView):
    model = CarModel
    template_name = "ctrl_comb/car-model-edit-modal.html"
    form_class = CarModelForm
    context_object_name = "object"
    success_url = reverse_lazy("control:model_list")
