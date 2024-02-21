from django.urls import path
from .views import *

urlpatterns = [
    path("brand", ListBrands.as_view(), name="brand_list"),
    path("brand/save", save_brand, name="save_brand"),
    path("brand/delete/<int:id>", delete_brand, name="delete_brand"),
    path("brand/edit/<int:id>", edit_brand, name="edit_brand"),
]
