
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404

from accounts.models import CustomUser
from .models import Livestock
from .forms import LivestockForm


def get_user_livestock(user):
    """
    Admin can access all livestock.
    Farmers can access only their own livestock.
    """

    if user.role == CustomUser.Role.ADMIN:
        return Livestock.objects.all()

    return Livestock.objects.filter(owner=user)


@login_required
def livestock_list(request):
    livestock_records = get_user_livestock(request.user)

    search_query = request.GET.get("search", "").strip()

    if search_query:
        livestock_records = livestock_records.filter(
            tag_number__icontains=search_query
        ) | livestock_records.filter(
            name__icontains=search_query
        ) | livestock_records.filter(
            breed__icontains=search_query
        )

    return render(
        request,
        "livestock/livestock_list.html",
        {
            "livestock_records": livestock_records,
            "search_query": search_query,
        }
    )


@login_required
def livestock_create(request):

    if request.method == "POST":
        form = LivestockForm(request.POST)

        if form.is_valid():
            livestock = form.save(commit=False)

            # Automatically assign the logged-in user as owner.
            # Admin-created records are also assigned to the admin.
            livestock.owner = request.user

            livestock.save()

            messages.success(
                request,
                "Livestock record successfully registered!"
            )

            return redirect("livestock_list")

    else:
        form = LivestockForm()

    return render(
        request,
        "livestock/livestock_form.html",
        {
            "form": form,
            "page_title": "Register Livestock",
            "button_text": "Register Livestock",
        }
    )


@login_required
def livestock_update(request, pk):

    livestock = get_object_or_404(
        get_user_livestock(request.user),
        pk=pk
    )

    if request.method == "POST":
        form = LivestockForm(
            request.POST,
            instance=livestock
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Livestock record successfully updated!"
            )

            return redirect("livestock_list")

    else:
        form = LivestockForm(instance=livestock)

    return render(
        request,
        "livestock/livestock_form.html",
        {
            "form": form,
            "page_title": "Update Livestock",
            "button_text": "Save Changes",
        }
    )


@login_required
def livestock_delete(request, pk):

    livestock = get_object_or_404(
        get_user_livestock(request.user),
        pk=pk
    )

    if request.method == "POST":
        livestock.delete()

        messages.success(
            request,
            "Livestock record successfully deleted!"
        )

        return redirect("livestock_list")

    return render(
        request,
        "livestock/livestock_confirm_delete.html",
        {"livestock": livestock}
    )
