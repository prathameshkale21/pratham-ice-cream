from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from home.models import Product, Category


from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from home.models import Product, Category


def product_list(request):

    products = Product.objects.filter(available=True)
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

    context = {
        "products": products,
        "categories": categories,
    }

    return render(
        request,
        "products/product_list.html",
        context
    )




def product_detail(request, slug):

    product = get_object_or_404(Product, slug=slug)

    related_products = Product.objects.filter(
        category=product.category,
        available=True
    ).exclude(id=product.id)[:4]

    return render(
        request,
        "products/product_detail.html",
        {
            "product": product,
            "related_products": related_products,
        }
    )