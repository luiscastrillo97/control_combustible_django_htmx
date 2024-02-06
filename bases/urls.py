from django.urls import path, include
from .views import *

app_name = "core"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("ejemplo", first_view, name="first_view"),
]
