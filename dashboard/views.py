
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from accounts.models import CustomUser


@login_required
def dashboard_redirect(request):
    """
    Redirect users to their appropriate dashboard.
    """

    if request.user.role == CustomUser.Role.ADMIN:
        return redirect("admin_dashboard")

    elif request.user.role == CustomUser.Role.FARMER:
        return redirect("farmer_dashboard")

    messages.error(request, "Your account has an invalid role.")
    return redirect("login")


@login_required
def admin_dashboard(request):
    """
    Admin-only dashboard.
    """

    if request.user.role != CustomUser.Role.ADMIN:
        messages.error(request, "You are not authorized to access that page.")
        return redirect("dashboard")

    return render(
        request,
        "dashboard/admin_dashboard.html"
    )


@login_required
def farmer_dashboard(request):
    """
    Farmer-only dashboard.
    """

    if request.user.role != CustomUser.Role.FARMER:
        messages.error(request, "You are not authorized to access that page.")
        return redirect("dashboard")

    return render(
        request,
        "dashboard/farmer_dashboard.html"
    )
