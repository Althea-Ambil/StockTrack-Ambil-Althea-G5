
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect


def home(request):
    return redirect("login")


urlpatterns = [
    path("", home, name="home"),
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("dashboard/", include("dashboard.urls")),
    path("livestock/", include("livestock.urls")),
]
