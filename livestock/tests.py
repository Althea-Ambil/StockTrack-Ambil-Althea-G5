
from datetime import date, timedelta
from decimal import Decimal

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from accounts.models import CustomUser
from .forms import LivestockForm
from .models import Livestock


class LivestockFormTests(TestCase):

    def setUp(self):
        self.valid_data = {
            "tag_number": "PIG-001",
            "name": "Bacon",
            "breed": "Large White",
            "sex": Livestock.Sex.MALE,
            "birth_date": date(2024, 1, 1),
            "weight": Decimal("25.50"),
            "acquisition_date": date(2024, 2, 1),
            "status": Livestock.Status.ACTIVE,
        }

    def test_valid_livestock_form(self):
        form = LivestockForm(data=self.valid_data)
        self.assertTrue(form.is_valid())

    def test_required_fields_cannot_be_empty(self):
        data = self.valid_data.copy()
        data["name"] = ""

        form = LivestockForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn("name", form.errors)

    def test_zero_weight_is_invalid(self):
        data = self.valid_data.copy()
        data["weight"] = "0"

        form = LivestockForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn("weight", form.errors)

    def test_future_birth_date_is_invalid(self):
        data = self.valid_data.copy()
        data["birth_date"] = timezone.localdate() + timedelta(days=1)

        form = LivestockForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn("birth_date", form.errors)

    def test_acquisition_before_birth_is_invalid(self):
        data = self.valid_data.copy()
        data["birth_date"] = date(2024, 5, 1)
        data["acquisition_date"] = date(2024, 4, 1)

        form = LivestockForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn("acquisition_date", form.errors)


class LivestockAccessTests(TestCase):

    def setUp(self):
        self.farmer = CustomUser.objects.create_user(
            username="farmer1",
            email="farmer1@example.com",
            password="TestPassword123!",
            role=CustomUser.Role.FARMER,
        )

        self.other_farmer = CustomUser.objects.create_user(
            username="farmer2",
            email="farmer2@example.com",
            password="TestPassword123!",
            role=CustomUser.Role.FARMER,
        )

        self.admin = CustomUser.objects.create_user(
            username="admin1",
            email="admin1@example.com",
            password="TestPassword123!",
            role=CustomUser.Role.ADMIN,
        )

        self.livestock = Livestock.objects.create(
            tag_number="PIG-100",
            name="Bacon",
            breed="Large White",
            sex=Livestock.Sex.MALE,
            birth_date=date(2024, 1, 1),
            weight=Decimal("25.50"),
            acquisition_date=date(2024, 2, 1),
            status=Livestock.Status.ACTIVE,
            owner=self.other_farmer,
        )

    def test_unauthenticated_user_is_redirected_to_login(self):
        response = self.client.get(reverse("livestock_list"))

        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse("login"), response.url)

    def test_farmer_cannot_update_another_farmers_record(self):
        self.client.login(
            username="farmer1",
            password="TestPassword123!",
        )

        response = self.client.get(
            reverse("livestock_update", kwargs={"pk": self.livestock.pk})
        )

        self.assertEqual(response.status_code, 404)

    def test_farmer_cannot_delete_another_farmers_record(self):
        self.client.login(
            username="farmer1",
            password="TestPassword123!",
        )

        response = self.client.post(
            reverse("livestock_delete", kwargs={"pk": self.livestock.pk})
        )

        self.assertEqual(response.status_code, 404)
        self.assertTrue(
            Livestock.objects.filter(pk=self.livestock.pk).exists()
        )

    def test_admin_can_access_another_farmers_record(self):
        self.client.login(
            username="admin1",
            password="TestPassword123!",
        )

        response = self.client.get(
            reverse("livestock_update", kwargs={"pk": self.livestock.pk})
        )

        self.assertEqual(response.status_code, 200)

    def test_invalid_livestock_id_returns_404(self):
        self.client.login(
            username="farmer1",
            password="TestPassword123!",
        )

        response = self.client.get(
            reverse("livestock_update", kwargs={"pk": 999999})
        )

        self.assertEqual(response.status_code, 404)
