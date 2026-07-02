from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from home.models import Product
from .models import WishlistItem


@login_required
def wishlist_view(request):

    items = WishlistItem.objects.filter(
        user=request.user
    ).select_related("product")

    return render(
        request,
        "wishlist/wishlist.html",
        {"items": items},
    )


@login_required
def add_to_wishlist(request, product_id):

    product = get_object_or_404(Product, id=product_id)

    item, created = WishlistItem.objects.get_or_create(
        user=request.user,
        product=product
    )

    if created:
        messages.success(
            request,
            f"❤️ {product.name} added to your wishlist."
        )
    else:
        messages.info(
            request,
            f"{product.name} is already in your wishlist."
        )

    return redirect(request.META.get("HTTP_REFERER", "wishlist:wishlist"))


@login_required
def remove_from_wishlist(request, item_id):

    item = get_object_or_404(
        WishlistItem,
        id=item_id,
        user=request.user
    )

    product_name = item.product.name
    item.delete()

    messages.success(
        request,
        f"Removed {product_name} from your wishlist."
    )

    return redirect("wishlist:wishlist")
