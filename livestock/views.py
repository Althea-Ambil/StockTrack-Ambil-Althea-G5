
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.db import transaction
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from accounts.models import CustomUser
from .models import Livestock
from .forms import LivestockForm


def get_user_livestock(user):
    """
    Admin can access all livestock.
    Farmers can access only their own livestock.
    Other roles are not allowed.
    """

    if user.role == CustomUser.Role.ADMIN:
        return Livestock.objects.select_related("owner").all()

    if user.role == CustomUser.Role.FARMER:
        return Livestock.objects.select_related("owner").filter(owner=user)

    raise PermissionDenied("You are not allowed to access livestock records.")


@login_required
def livestock_list(request):
    livestock_records = get_user_livestock(request.user)

    search_query = request.GET.get("search", "").strip()

    if search_query:
        livestock_records = livestock_records.filter(
            Q(tag_number__icontains=search_query)
            | Q(name__icontains=search_query)
            | Q(breed__icontains=search_query)
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
    get_user_livestock(request.user)

    if request.method == "POST":
        form = LivestockForm(request.POST)

        if form.is_valid():
            with transaction.atomic():
                livestock = form.save(commit=False)
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
        form = LivestockForm(request.POST, instance=livestock)

        if form.is_valid():
            with transaction.atomic():
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
        with transaction.atomic():
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
