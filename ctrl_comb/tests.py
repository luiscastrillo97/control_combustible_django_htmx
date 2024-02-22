from django.test import TestCase
from django.urls import reverse
from .models import *


class ModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.model = CarModel.objects.create(
            brand=Brand.objects.create(description="Ford"), description="Mustang"
        )

    def test_list_models(self):
        self.assertEqual(self.model.description, "Mustang")
        self.assertEqual(self.model.brand.description, "Ford")

    def test_model_view(self):
        response = self.client.get(reverse("control:model_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Mustang")
        self.assertTemplateUsed(response, "ctrl_comb/car-model.html")

    def test_brand_view(self):
        response = self.client.get(reverse("control:brand_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ford")
        self.assertTemplateUsed(response, "ctrl_comb/brand.html")

    def test_edit_model_modal(self):
        response = self.client.get(
            reverse("control:update_model_modal", kwargs={"pk": self.model.id})
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Mustang")
        self.assertContains(response, "Editar")
        self.assertTemplateUsed(response, "ctrl_comb/car-model-edit-modal.html")

    def test_create_model_modal(self):
        response = self.client.get(reverse("control:create_model_modal"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Agregar")
        self.assertContains(response, "Ford")
        self.assertTemplateUsed(response, "ctrl_comb/car-model-edit-modal.html")
