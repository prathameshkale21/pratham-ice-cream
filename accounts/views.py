from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm


def register_view(request):

    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save()
            login(request, user)

            messages.success(
                request,
                f"🎉 Welcome {user.username}! Your account has been created."
            )

            return redirect("home")

        else:
            messages.error(
                request,
                "Please fix the errors below and try again."
            )

    else:
        form = RegisterForm()

    return render(
        request,
        "accounts/register.html",
        {"form": form},
    )


def login_view(request):

    if request.user.is_authenticated:
        return redirect("home")

    next_url = request.POST.get("next") or request.GET.get("next")

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:

            login(request, user)

            messages.success(
                request,
                f"👋 Welcome back, {user.username}!"
            )

            return redirect(next_url or "home")

        else:
            messages.error(
                request,
                "Invalid username or password. Please try again."
            )

    return render(
        request,
        "accounts/login.html",
        {"next": next_url},
    )


@login_required
def logout_view(request):

    logout(request)

    messages.info(
        request,
        "You have been logged out. See you soon! 🍦"
    )

    return redirect("home")
