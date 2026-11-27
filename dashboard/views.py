
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect

from accounts.models import CustomUser


@login_required
def dashboard_redirect(request):
    """
    Redirect users to their appropriate dashboard.
    """

    if request.user.role == CustomUser.Role.ADMIN:
        return redirect("admin_dashboard")

    if request.user.role == CustomUser.Role.FARMER:
        return redirect("farmer_dashboard")

    messages.error(request, "Your account has an invalid role.")
    raise PermissionDenied("Your account does not have a valid role.")


@login_required
def admin_dashboard(request):
    """
    Admin-only dashboard.
    """

    if request.user.role != CustomUser.Role.ADMIN:
        messages.error(
            request,
            "You are not authorized to access that page."
        )
        raise PermissionDenied(
            "Only administrators can access this dashboard."
        )

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
        messages.error(
            request,
            "You are not authorized to access that page."
        )
        raise PermissionDenied(
            "Only farmers can access this dashboard."
        )

    return render(
        request,
        "dashboard/farmer_dashboard.html"
    )
