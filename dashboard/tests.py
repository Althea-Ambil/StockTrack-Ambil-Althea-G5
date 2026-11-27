
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


class DashboardAccessTests(TestCase):

    def setUp(self):
        self.admin = User.objects.create_user(
            username="admin_test",
            email="admin@example.com",
            password="StrongPass123!",
            role=User.Role.ADMIN
        )

        self.farmer = User.objects.create_user(
            username="farmer_test",
            email="farmer@example.com",
            password="StrongPass123!",
            role=User.Role.FARMER
        )

    def test_admin_can_access_admin_dashboard(self):
        self.client.force_login(self.admin)

        response = self.client.get(reverse("admin_dashboard"))

        self.assertEqual(response.status_code, 200)

    def test_farmer_cannot_access_admin_dashboard(self):
        self.client.force_login(self.farmer)

        response = self.client.get(reverse("admin_dashboard"))

        self.assertEqual(response.status_code, 403)

    def test_farmer_can_access_farmer_dashboard(self):
        self.client.force_login(self.farmer)

        response = self.client.get(reverse("farmer_dashboard"))

        self.assertEqual(response.status_code, 200)

    def test_admin_cannot_access_farmer_dashboard(self):
        self.client.force_login(self.admin)

        response = self.client.get(reverse("farmer_dashboard"))

        self.assertEqual(response.status_code, 403)

    def test_dashboard_redirects_admin_correctly(self):
        self.client.force_login(self.admin)

        response = self.client.get(reverse("dashboard"))

        self.assertRedirects(
            response,
            reverse("admin_dashboard")
        )

    def test_dashboard_redirects_farmer_correctly(self):
        self.client.force_login(self.farmer)

        response = self.client.get(reverse("dashboard"))

        self.assertRedirects(
            response,
            reverse("farmer_dashboard")
        )

    def test_admin_dashboard_requires_login(self):
        response = self.client.get(reverse("admin_dashboard"))

        self.assertEqual(response.status_code, 302)
        self.assertIn("/accounts/login/", response.url)

    def test_farmer_dashboard_requires_login(self):
        response = self.client.get(reverse("farmer_dashboard"))

        self.assertEqual(response.status_code, 302)
        self.assertIn("/accounts/login/", response.url)

    def test_dashboard_redirect_requires_login(self):
        response = self.client.get(reverse("dashboard"))

        self.assertEqual(response.status_code, 302)
        self.assertIn("/accounts/login/", response.url)
