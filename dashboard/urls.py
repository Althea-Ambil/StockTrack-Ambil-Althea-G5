
from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard_redirect, name="dashboard"),

    path(
        "admin/",
        views.admin_dashboard,
        name="admin_dashboard"
    ),

    path(
        "farmer/",
        views.farmer_dashboard,
        name="farmer_dashboard"
    ),
]
