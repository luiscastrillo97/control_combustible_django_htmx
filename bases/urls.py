from django.urls import path, include
from .views import *

app_name = "core"

urlpatterns = [
    path("", first_view, name="first_view"),
]
