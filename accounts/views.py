
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import FarmerRegistrationForm, ProfileUpdateForm


def register(request):

    if request.method == "POST":
        form = FarmerRegistrationForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Your StockTrack account has been created successfully!"
            )

            return redirect("login")

    else:
        form = FarmerRegistrationForm()

    return render(
        request,
        "accounts/register.html",
        {"form": form}
    )


@login_required
def profile(request):

    if request.method == "POST":

        form = ProfileUpdateForm(
            request.POST,
            instance=request.user
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Your profile has been updated successfully!"
            )

            return redirect("profile")

        else:

            messages.error(
                request,
                "Please correct the errors below."
            )

    else:

        form = ProfileUpdateForm(
            instance=request.user
        )

    return render(
        request,
        "accounts/profile.html",
        {"form": form}
    )
