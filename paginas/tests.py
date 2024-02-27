from django.test import SimpleTestCase
from django.urls import reverse


class AboutPageTests(SimpleTestCase):
    databases = {"default"}

    def setUp(self):
        self.response = self.client.get("/pages/about")

    def test_exists_url(self):
        self.assertEqual(self.response.status_code, 200)

    def test_html_content(self):
        self.assertTemplateUsed(self.response, "paginas/about.html")
        self.assertContains(self.response, "Acerca de la aplicación")
        self.assertNotContains(self.response, "El lucho")
