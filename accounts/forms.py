
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
        email = self.cleaned_data.get("email")

        if CustomUser.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError(
                "This email address is already registered."
            )

        return email.lower()

    def save(self, commit=True):
        user = super().save(commit=False)

        user.role = CustomUser.Role.FARMER

        if commit:
            user.save()

        return user
