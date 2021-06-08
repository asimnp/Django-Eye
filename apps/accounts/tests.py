from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomUserTests(TestCase):

    def test_create_user(self):
        user = User.objects.create_user(
            username='alex',
            email='alex@email.com',
            password='password123'
        )

        self.assertEqual(user.username, 'alex')
        self.assertEqual(user.email, 'alex@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        admin_user = User.objects.create_superuser(
            username='admin',
            email='admin@email.com',
            password='password123'
        )

        self.assertEqual(admin_user.username, 'admin')
        self.assertEqual(admin_user.email, 'admin@email.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
