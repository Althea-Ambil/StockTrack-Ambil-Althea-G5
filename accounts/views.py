
from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import FarmerRegistrationForm


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
