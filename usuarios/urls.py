from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import *

app_name = "users"

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path(
        "login-alt/",
        auth_views.LoginView.as_view(template_name="usuarios/login_alt.html"),
        name="login_alt",
    ),
    path("register/", RegisterUserView.as_view(), name="register"),
]
