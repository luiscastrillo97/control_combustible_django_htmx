from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse

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


def datatable_model(request):
    context = {}
    data = request.GET

    draw = int(data.get("draw"))
    start = int(data.get("start"))
    length = int(data.get("length"))
    search = data.get("search[value]")

    records = CarModel.objects.all()
    records_total = records.count()

    if search:
        records = records.filter(
            Q(brand__description__icontains=search) | Q(description__icontains=search)
        )

    records_filtered = records.count()

    context["draw"] = draw
    context["recordsTotal"] = records_total
    context["recordsFiltered"] = records_filtered

    object_list = records[start : (start + length)]
    paginator = Paginator(object_list, length)

    try:
        objects = paginator.page(draw).object_list
    except PageNotAnInteger:
        objects = paginator.page(int(draw)).object_list
    except EmptyPage:
        objects = paginator.page(paginator.num_pages).object_list

    data_to_send = [
        {
            "id": object.id,
            "brand": object.brand.description,
            "description": object.description,
        }
        for object in objects
    ]

    context["data"] = data_to_send

    return JsonResponse(context, safe=False)
