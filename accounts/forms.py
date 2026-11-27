
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class FarmerRegistrationForm(UserCreationForm):

    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser

        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "contact_number",
            "password1",
            "password2",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            label = field.label or field_name.replace("_", " ")

            field.widget.attrs.update({
                "class": "form-control",
                "placeholder": f"Enter {label.lower()}",
            })

    def clean_email(self):
        email = self.cleaned_data.get("email", "").strip().lower()

        if CustomUser.objects.filter(
            email__iexact=email
        ).exists():
            raise forms.ValidationError(
                "This email address is already registered."
            )

        return email

    def save(self, commit=True):
        user = super().save(commit=False)

        user.role = CustomUser.Role.FARMER

        if commit:
            user.save()

        return user


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = CustomUser

        fields = [
            "first_name",
            "last_name",
            "email",
            "contact_number",
        ]

        widgets = {
            "first_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter your first name",
            }),

            "last_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter your last name",
            }),

            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Enter your email",
            }),

            "contact_number": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter your contact number",
            }),
        }

    def clean_email(self):
        email = self.cleaned_data["email"].strip().lower()

        existing_user = CustomUser.objects.filter(
            email__iexact=email
        ).exclude(
            pk=self.instance.pk
        )

        if existing_user.exists():
            raise forms.ValidationError(
                "This email address is already being used."
            )

        return email

    def clean_first_name(self):
        first_name = self.cleaned_data["first_name"].strip()

        if not first_name:
            raise forms.ValidationError(
                "First name cannot be empty."
            )

        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data["last_name"].strip()

        if not last_name:
            raise forms.ValidationError(
                "Last name cannot be empty."
            )

        return last_name
