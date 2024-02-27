from django.test import TestCase


class HomePageTests(TestCase):

    def setUp(self):
        self.response = self.client.get("/")

    def test_exists_url(self):
        self.assertEqual(self.response.status_code, 200)

    def test_html_content(self):
        self.assertTemplateUsed(self.response, "bases/home.html")
        self.assertContains(self.response, "Bienvenido")
        self.assertNotContains(self.response, "Acerca de la App")
