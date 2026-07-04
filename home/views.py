from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Carousel, Category, Product, Feedback

def home(request):

    carousel = Carousel.objects.filter(active=True)

    categories = Category.objects.all()

    featured_products = Product.objects.filter(
        featured=True,
        available=True
    ).select_related("category")

    latest_products = Product.objects.filter(
        available=True
    ).select_related("category").order_by("-created_at")[:8]

    return render(request, "home/index.html", {
        "carousel": carousel,
        "categories": categories,
        "featured_products": featured_products,
        "latest_products": latest_products,
    })


def about(request):
    return render(request, "about.html")


def privacy_policy(request):
    return render(request, "privacy_policy.html")


def feedback_view(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("desc")

        Feedback.objects.create(
            name=name,
            email=email,
            phone=phone,
            desc=desc,
        )

        messages.success(
            request,
            "💬 Thanks for your feedback! We appreciate you taking the time."
        )

        return redirect("feedback")

    return render(request, "feedback.html")

