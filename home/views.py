from django.shortcuts import render
from .models import Carousel, Category, Product

def home(request):

    carousel = Carousel.objects.filter(active=True)

    categories = Category.objects.all()

    featured_products = Product.objects.filter(
        featured=True,
        available=True
    )

    latest_products = Product.objects.filter(
        available=True
    ).order_by("-created_at")[:8]

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

