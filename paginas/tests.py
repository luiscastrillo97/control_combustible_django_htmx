from django.test import SimpleTestCase
from django.urls import reverse


class AboutPageTests(SimpleTestCase):
    # With DRY
    def setUp(self):
        self.response = self.client.get("/pages/about/")

    def test_exists_url(self):
        self.assertEqual(self.response.status_code, 200)

    def test_html_content(self):
        self.assertTemplateUsed(self.response, "paginas/about.html")
        self.assertContains(
            self.response, "Aplicación para controlar el gasto de los combustibles"
        )
        self.assertNotContains(self.response, "El lucho")

    """
    # Without DRY

    def test_exists_about_url(self):
        response = self.client.get("/pages/about/")
        self.assertEqual(response.status_code, 200)

    def test_about_url_name(self):
        response = self.client.get(reverse("pages:about-app"))
        self.assertEqual(response.status_code, 200)

    def test_template_contains(self):
        response = self.client.get("/pages/about/")
        self.assertContains(
            response, "Aplicación para controlar el gasto de los combustibles"
        )

    def test_template_not_contains(self):
        response = self.client.get("/pages/about/")
        self.assertNotContains(response, "El lucho")
    """
