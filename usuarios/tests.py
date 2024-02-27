from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve
from .forms import CustomUserCreationForm
from .views import RegisterUserView


class CustomUserTest(TestCase):
    def test_crear_usuario(self):
        Usr = get_user_model()
        usr = Usr.objects.create_user(
            username="test1",
            email="test1@gmail.com",
            password="12345678",
            first_name="testU1",
        )

        self.assertEqual(usr.username, "test1")
        self.assertEqual(usr.first_name, "testU1")
        self.assertEqual(usr.email, "test1@gmail.com")
        self.assertTrue(usr.is_active)
        self.assertFalse(usr.is_staff)
        self.assertFalse(usr.is_superuser)

    def test_crear_superusuario(self):
        Usr = get_user_model()
        usr = Usr.objects.create_superuser(
            username="superuser1",
            email="superuser1@gmail.com",
            password="12345678",
            first_name="superU1",
        )

        self.assertEqual(usr.username, "superuser1")
        self.assertEqual(usr.first_name, "superU1")
        self.assertEqual(usr.email, "superuser1@gmail.com")
        self.assertTrue(usr.is_active)
        self.assertTrue(usr.is_staff)
        self.assertTrue(usr.is_superuser)


class UserRegisterTest(TestCase):
    def setUp(self):
        url = reverse("users:register")
        self.response = self.client.get(url)
        self.form = self.response.context.get("form")
        self.view = resolve("/users/register/")

    def test_register_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "usuarios/register.html")
        self.assertContains(self.response, "Registrar")
        self.assertNotContains(self.response, "Bienvenido")

    def test_register_form(self):
        self.assertIsInstance(self.form, CustomUserCreationForm)
        self.assertContains(self.response, "X-CSRFToken")

    def test_register_view(self):
        self.assertEqual(self.view.func.__name__, RegisterUserView.as_view().__name__)
