from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from home.models import Product, Category


def product_list(request):

    products = Product.objects.filter(available=True).select_related("category")
    categories = Category.objects.all()

    # Search
    search = request.GET.get("search")

    if search:
        products = products.filter(
            Q(name__icontains=search) |
            Q(description__icontains=search)
        )

    # Category Filter
    category = request.GET.get("category")

    if category:
        products = products.filter(category_id=category)

    # Sort
    sort = request.GET.get("sort")

    if sort == "low":
        products = products.order_by("price")

    elif sort == "high":
        products = products.order_by("-price")

    elif sort == "latest":
        products = products.order_by("-created_at")

    elif sort == "name":
        products = products.order_by("name")

    # Pagination — keeps each page light and fast to load
    paginator = Paginator(products, 12)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "products": page_obj,
        "page_obj": page_obj,
        "categories": categories,
    }

    return render(
        request,
        "products/product_list.html",
        context
    )


def product_detail(request, slug):

    product = get_object_or_404(
        Product.objects.select_related("category"),
        slug=slug
    )

    related_products = Product.objects.filter(
        category=product.category,
        available=True
    ).select_related("category").exclude(id=product.id)[:4]

    return render(
        request,
        "products/product_detail.html",
        {
            "product": product,
            "related_products": related_products,
        }
    )