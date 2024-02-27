from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required

from .models import *
from .forms import *
from bases.views import LoginAndPermissionRequiredMixin, CreateOrModifyMixin


class ListBrands(LoginAndPermissionRequiredMixin, ListView):
    template_name = "ctrl_comb/brand.html"
    model = Brand
    context_object_name = "objects"
    ordering = ["description"]
    login_url = "users:login_alt"
    permission_required = "ctrl_comb.view_brand"


@login_required(login_url="users:login_alt")
def save_brand(request):
    context = {}
    template_name = "ctrl_comb/brand-list.html"

    if request.method == "POST":
        user_id = request.user
        id = request.POST.get("id")
        description = request.POST.get("description")
        brand = None

        if id:
            brand = Brand.objects.filter(id=id).first()
        else:
            brand = Brand.objects.filter(description=description).first()

        if brand:
            brand.description = description
            brand.modified_by = user_id
            brand.save()
        else:
            brand = Brand.objects.create(description=description, created_by=user_id)

    objects = Brand.objects.all().order_by("description")
    context["register"] = brand
    context["objects"] = objects

    return render(request, template_name, context)


@login_required(login_url="users:login_alt")
def delete_brand(request, id):
    context = {}
    template_name = "ctrl_comb/brand-list.html"

    object_to_eliminate = Brand.objects.filter(id=id).first()
    object_to_eliminate.delete()

    objects = Brand.objects.all().order_by("description")
    context["objects"] = objects

    return render(request, template_name, context)


@login_required(login_url="users:login_alt")
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


class ListCarModels(LoginAndPermissionRequiredMixin, ListView):
    model = CarModel
    template_name = "ctrl_comb/car-model.html"
    context_object_name = "objects"
    ordering = ["brand", "description"]
    login_url = "users:login_alt"
    permission_required = "ctrl_comb.view_carmodel"
    # permission_required = "ctrl_comb.read_write_permission"


class CreateCarModel(LoginAndPermissionRequiredMixin, CreateOrModifyMixin, CreateView):
    model = CarModel
    template_name = "ctrl_comb/car-model-form.html"
    form_class = CarModelForm
    context_object_name = "object"
    success_url = reverse_lazy("control:model_list")
    permission_required = "ctrl_comb.add_carmodel"


class UpdateCarModel(LoginRequiredMixin, UpdateView):
    model = CarModel
    template_name = "ctrl_comb/car-model-form.html"
    form_class = CarModelForm
    context_object_name = "object"
    success_url = reverse_lazy("control:model_list")
    login_url = "users:login_alt"


class DeleteCarModel(LoginRequiredMixin, DeleteView):
    model = CarModel
    template_name = "bases/delete.html"
    context_object_name = "object"
    success_url = reverse_lazy("control:model_list")
    login_url = "users:login_alt"


class UpdateCarModelWithModal(
    LoginAndPermissionRequiredMixin, CreateOrModifyMixin, UpdateView
):
    model = CarModel
    template_name = "ctrl_comb/car-model-edit-modal.html"
    form_class = CarModelForm
    context_object_name = "object"
    success_url = reverse_lazy("control:model_list")
    permission_required = "ctrl_comb.change_carmodel"


class CreateCarModelWithModal(LoginRequiredMixin, CreateView):
    model = CarModel
    template_name = "ctrl_comb/car-model-edit-modal.html"
    form_class = CarModelForm
    context_object_name = "object"
    success_url = reverse_lazy("control:model_list")


@login_required(login_url="users:login_alt")
@permission_required(perm="ctrl_comb.view_carmodel")
# @permission_required(perm="ctrl_comb.read_write_permission")
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
