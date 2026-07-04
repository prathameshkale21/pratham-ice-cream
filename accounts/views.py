from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import RegisterForm
from .models import SecurityProfile


def register_view(request):

    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save()

            profile = SecurityProfile(
                user=user,
                question=form.cleaned_data["security_question"],
            )
            profile.set_answer(form.cleaned_data["security_answer"])
            profile.save()

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


def forgot_password_view(request):
    """Step 1: enter your username."""

    if request.method == "POST":

        username = request.POST.get("username", "").strip()

        try:
            user = User.objects.get(username=username)
            user.security_profile  # will raise if missing

        except (User.DoesNotExist, SecurityProfile.DoesNotExist):
            messages.error(
                request,
                "We couldn't find an account with that username and a "
                "security question set up."
            )
            return redirect("accounts:forgot_password")

        request.session["reset_username"] = username

        return redirect("accounts:verify_security_question")

    return render(request, "accounts/forgot_password.html")


def verify_security_question_view(request):
    """Step 2: answer the security question."""

    username = request.session.get("reset_username")

    if not username:
        messages.error(request, "Please start the password reset process again.")
        return redirect("accounts:forgot_password")

    try:
        user = User.objects.get(username=username)
        profile = user.security_profile

    except (User.DoesNotExist, SecurityProfile.DoesNotExist):
        messages.error(request, "Something went wrong. Please try again.")
        return redirect("accounts:forgot_password")

    if request.method == "POST":

        answer = request.POST.get("answer", "")

        if profile.check_answer(answer):
            request.session["reset_verified"] = True
            return redirect("accounts:reset_password")

        else:
            messages.error(request, "That answer doesn't match our records.")

    return render(
        request,
        "accounts/verify_security_question.html",
        {"question": profile.get_question_text()},
    )


def reset_password_view(request):
    """Step 3: set a new password."""

    username = request.session.get("reset_username")
    verified = request.session.get("reset_verified")

    if not username or not verified:
        messages.error(request, "Please start the password reset process again.")
        return redirect("accounts:forgot_password")

    if request.method == "POST":

        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if not password1 or password1 != password2:
            messages.error(request, "Passwords do not match.")

        elif len(password1) < 8:
            messages.error(request, "Password must be at least 8 characters long.")

        else:
            try:
                user = User.objects.get(username=username)

            except User.DoesNotExist:
                messages.error(request, "Something went wrong. Please try again.")
                return redirect("accounts:forgot_password")

            user.set_password(password1)
            user.save()

            del request.session["reset_username"]
            del request.session["reset_verified"]

            messages.success(
                request,
                "🔐 Your password has been reset. Please log in."
            )

            return redirect("accounts:login")

    return render(request, "accounts/reset_password.html")
