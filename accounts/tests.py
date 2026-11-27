
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .forms import FarmerRegistrationForm, ProfileUpdateForm

User = get_user_model()


class FarmerRegistrationFormTests(TestCase):

    def test_valid_registration(self):
        form = FarmerRegistrationForm(data={
            "username": "farmer1",
            "email": "farmer1@example.com",
            "first_name": "John",
            "last_name": "Doe",
            "contact_number": "09123456789",
            "password1": "StrongPass123!",
            "password2": "StrongPass123!",
        })

        self.assertTrue(form.is_valid(), form.errors)

    def test_duplicate_email_is_rejected(self):
        User.objects.create_user(
            username="existing",
            email="farmer@example.com",
            password="StrongPass123!"
        )

        form = FarmerRegistrationForm(data={
            "username": "newfarmer",
            "email": "FARMER@example.com",
            "first_name": "Jane",
            "last_name": "Doe",
            "contact_number": "",
            "password1": "StrongPass123!",
            "password2": "StrongPass123!",
        })

        self.assertFalse(form.is_valid())
        self.assertIn("email", form.errors)

    def test_registration_assigns_farmer_role(self):
        form = FarmerRegistrationForm(data={
            "username": "newfarmer",
            "email": "newfarmer@example.com",
            "first_name": "Jane",
            "last_name": "Doe",
            "contact_number": "",
            "password1": "StrongPass123!",
            "password2": "StrongPass123!",
        })

        self.assertTrue(form.is_valid(), form.errors)

        user = form.save()

        self.assertEqual(user.role, User.Role.FARMER)


class ProfileUpdateFormTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="farmer1",
            email="farmer1@example.com",
            password="StrongPass123!",
            first_name="John",
            last_name="Doe"
        )

    def test_valid_profile_update(self):
        form = ProfileUpdateForm(
            data={
                "first_name": "Updated",
                "last_name": "Farmer",
                "email": "updated@example.com",
                "contact_number": "09123456789",
            },
            instance=self.user
        )

        self.assertTrue(form.is_valid(), form.errors)

    def test_blank_first_name_is_rejected(self):
        form = ProfileUpdateForm(
            data={
                "first_name": "   ",
                "last_name": "Doe",
                "email": self.user.email,
                "contact_number": "",
            },
            instance=self.user
        )

        self.assertFalse(form.is_valid())
        self.assertIn("first_name", form.errors)

    def test_blank_last_name_is_rejected(self):
        form = ProfileUpdateForm(
            data={
                "first_name": "John",
                "last_name": "   ",
                "email": self.user.email,
                "contact_number": "",
            },
            instance=self.user
        )

        self.assertFalse(form.is_valid())
        self.assertIn("last_name", form.errors)

    def test_duplicate_email_is_rejected(self):
        User.objects.create_user(
            username="farmer2",
            email="another@example.com",
            password="StrongPass123!"
        )

        form = ProfileUpdateForm(
            data={
                "first_name": "John",
                "last_name": "Doe",
                "email": "another@example.com",
                "contact_number": "",
            },
            instance=self.user
        )

        self.assertFalse(form.is_valid())
        self.assertIn("email", form.errors)

    def test_role_is_not_available_in_profile_form(self):
        form = ProfileUpdateForm(instance=self.user)

        self.assertNotIn("role", form.fields)


class ProfileAccessTests(TestCase):

    def test_profile_requires_login(self):
        response = self.client.get(reverse("profile"))

        self.assertEqual(response.status_code, 302)
        self.assertIn("/accounts/login/", response.url)
