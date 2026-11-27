
from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator


class Livestock(models.Model):

    class Sex(models.TextChoices):
        MALE = "MALE", "Male"
        FEMALE = "FEMALE", "Female"

    class Status(models.TextChoices):
        ACTIVE = "ACTIVE", "Active"
        SOLD = "SOLD", "Sold"
        DECEASED = "DECEASED", "Deceased"

    tag_number = models.CharField(
        max_length=30,
        unique=True
    )

    name = models.CharField(
        max_length=100
    )

    breed = models.CharField(
        max_length=100
    )

    sex = models.CharField(
        max_length=10,
        choices=Sex.choices
    )

    birth_date = models.DateField()

    weight = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(0.01)]
    )

    acquisition_date = models.DateField()

    status = models.CharField(
        max_length=15,
        choices=Status.choices,
        default=Status.ACTIVE
    )

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="livestock_records"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        constraints = [
            models.CheckConstraint(
                condition=models.Q(weight__gt=0),
                name="livestock_weight_positive"
            ),
            models.CheckConstraint(
                condition=models.Q(sex__in=["MALE", "FEMALE"]),
                name="livestock_valid_sex"
            ),
            models.CheckConstraint(
                condition=models.Q(
                    status__in=["ACTIVE", "SOLD", "DECEASED"]
                ),
                name="livestock_valid_status"
            ),
        ]

    def __str__(self):
        return f"{self.tag_number} - {self.name}"
