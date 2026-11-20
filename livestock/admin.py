
from django.contrib import admin
from .models import Livestock


@admin.register(Livestock)
class LivestockAdmin(admin.ModelAdmin):

    list_display = (
        "tag_number",
        "name",
        "breed",
        "sex",
        "weight",
        "status",
        "owner",
        "created_at",
    )

    list_filter = (
        "breed",
        "sex",
        "status",
    )

    search_fields = (
        "tag_number",
        "name",
        "breed",
        "owner__username",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )
