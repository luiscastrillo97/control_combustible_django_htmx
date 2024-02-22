from django.urls import path
from .views import *

urlpatterns = [
    path("brands", ListBrands.as_view(), name="brand_list"),
    path("brands/save", save_brand, name="save_brand"),
    path("brands/delete/<int:id>", delete_brand, name="delete_brand"),
    path("brands/edit/<int:id>", edit_brand, name="edit_brand"),
    path("models", ListCarModels.as_view(), name="model_list"),
    path("models/create", CreateCarModel.as_view(), name="create_model"),
    path("models/update/<int:pk>", UpdateCarModel.as_view(), name="update_model"),
    path("models/delete/<int:pk>", DeleteCarModel.as_view(), name="delete_model"),
    path(
        "models/create/modal",
        CreateCarModelWithModal.as_view(),
        name="create_model_modal",
    ),
    path(
        "models/update/modal/<int:pk>",
        UpdateCarModelWithModal.as_view(),
        name="update_model_modal",
    ),
]
