from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from .models import *


class ModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.model = CarModel.objects.create(
            brand=Brand.objects.create(description="Ford"), description="Mustang"
        )
        cls.user = get_user_model().objects.create_user(
            username="test6",
            email="test6@gmail.com",
            password="THEb0$$_",
            first_name="testU6",
        )
        cls.view_carmodel = Permission.objects.get(codename="view_carmodel")

    def test_view_model_logout(self):
        self.client.logout()
        response = self.client.get(reverse("control:model_list"))
        self.assertEqual(response.status_code, 302)

    def test_list_models(self):
        self.assertEqual(self.model.description, "Mustang")
        self.assertEqual(self.model.brand.description, "Ford")

    def test_model_view_authenticated_user(self):
        self.client.login(email="test6@gmail.com", password="THEb0$$_")
        self.user.user_permissions.add(self.view_carmodel)
        response = self.client.get(reverse("control:model_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Modelo")
        self.assertTemplateUsed(response, "ctrl_comb/car-model.html")

    def test_view_brand_logout(self):
        self.client.logout()
        response = self.client.get(reverse("control:brand_list"))
        self.assertEqual(response.status_code, 302)

    def test_brand_view(self):
        self.client.login(email="test6@gmail.com", password="THEb0$$_")
        response = self.client.get(reverse("control:brand_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ford")
        self.assertTemplateUsed(response, "ctrl_comb/brand.html")

    def test_edit_model_modal(self):
        self.client.login(email="test6@gmail.com", password="THEb0$$_")
        response = self.client.get(
            reverse("control:update_model_modal", kwargs={"pk": self.model.id})
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Mustang")
        self.assertContains(response, "Editar")
        self.assertTemplateUsed(response, "ctrl_comb/car-model-edit-modal.html")

    def test_create_model_modal(self):
        self.client.login(email="test6@gmail.com", password="THEb0$$_")
        response = self.client.get(reverse("control:create_model_modal"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Agregar")
        self.assertContains(response, "Ford")
        self.assertTemplateUsed(response, "ctrl_comb/car-model-edit-modal.html")
