
from django import forms
from django.utils import timezone

from .models import Livestock


class LivestockForm(forms.ModelForm):

    class Meta:
        model = Livestock

        fields = [
            "tag_number",
            "name",
            "breed",
            "sex",
            "birth_date",
            "weight",
            "acquisition_date",
            "status",
        ]

        widgets = {
            "tag_number": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Example: PIG-001",
            }),
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter pig name",
            }),
            "breed": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Example: Large White",
            }),
            "sex": forms.Select(attrs={
                "class": "form-select",
            }),
            "birth_date": forms.DateInput(attrs={
                "class": "form-control",
                "type": "date",
            }),
            "weight": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Enter weight in kilograms",
                "step": "0.01",
                "min": "0.01",
            }),
            "acquisition_date": forms.DateInput(attrs={
                "class": "form-control",
                "type": "date",
            }),
            "status": forms.Select(attrs={
                "class": "form-select",
            }),
        }

    def clean_tag_number(self):
        tag_number = self.cleaned_data.get("tag_number", "").strip().upper()

        if not tag_number:
            raise forms.ValidationError(
                "Livestock tag number is required."
            )

        existing = Livestock.objects.filter(
            tag_number__iexact=tag_number
        ).exclude(pk=self.instance.pk)

        if existing.exists():
            raise forms.ValidationError(
                "This livestock tag number is already registered."
            )

        return tag_number

    def clean_name(self):
        name = self.cleaned_data.get("name", "").strip()

        if not name:
            raise forms.ValidationError(
                "Livestock name is required."
            )

        return name

    def clean_breed(self):
        breed = self.cleaned_data.get("breed", "").strip()

        if not breed:
            raise forms.ValidationError(
                "Livestock breed is required."
            )

        return breed

    def clean_weight(self):
        weight = self.cleaned_data.get("weight")

        if weight is None:
            return weight

        if weight <= 0:
            raise forms.ValidationError(
                "Weight must be greater than zero."
            )

        return weight

    def clean(self):
        cleaned_data = super().clean()

        birth_date = cleaned_data.get("birth_date")
        acquisition_date = cleaned_data.get("acquisition_date")

        today = timezone.localdate()

        if birth_date and birth_date > today:
            self.add_error(
                "birth_date",
                "Birth date cannot be in the future."
            )

        if acquisition_date and acquisition_date > today:
            self.add_error(
                "acquisition_date",
                "Acquisition date cannot be in the future."
            )

        if birth_date and acquisition_date:
            if acquisition_date < birth_date:
                self.add_error(
                    "acquisition_date",
                    "Acquisition date cannot be earlier than birth date."
                )

        return cleaned_data
