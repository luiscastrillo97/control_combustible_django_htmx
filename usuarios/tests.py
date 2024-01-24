from django.test import TestCase
from django.contrib.auth import get_user_model


class CustomUserTest(TestCase):
    # Simulamos la creación de un usuario
    def test_crear_usuario(self):
        Usr = get_user_model()
        usr = Usr.objects.create_user(
            username="test1", email="test1@gmail.com", password="12345678"
        )

        # Qué esperamos de la prueba
        self.assertEqual(usr.username, "test1")
        self.assertEqual(usr.email, "test1@gmail.com")
        self.assertTrue(usr.is_active)
        self.assertFalse(usr.is_staff)
        self.assertFalse(usr.is_superuser)

    def test_crear_superusuario(self):
        Usr = get_user_model()
        usr = Usr.objects.create_superuser(
            username="superuser1", email="superuser1@gmail.com", password="12345678"
        )

        # Qué esperamos de la prueba
        self.assertEqual(usr.username, "superuser1")
        self.assertEqual(usr.email, "superuser1@gmail.com")
        self.assertTrue(usr.is_active)
        self.assertTrue(usr.is_staff)
        self.assertTrue(usr.is_superuser)
