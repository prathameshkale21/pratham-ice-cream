from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from cart.models import Cart, CartItem
from .models import Order, OrderItem


@login_required
def checkout(request):

    cart, created = Cart.objects.get_or_create(user=request.user)
    items = cart.items.all()

    if request.method == "POST":

        if not items:
            messages.error(request, "Your cart is empty.")
            return redirect("cart:cart")

        # Create the order and snapshot each cart item's price
        order = Order.objects.create(
            user=request.user,
            total=cart.total,
        )

        for item in items:
            unit_price = item.product.discount_price or item.product.price

            OrderItem.objects.create(
                order=order,
                product=item.product,
                price=unit_price,
                quantity=item.quantity,
            )

        # Empty the cart now that the order has been placed
        CartItem.objects.filter(cart=cart).delete()

        messages.success(
            request,
            "🎉 Your order has been placed successfully!"
        )

        return redirect("orders:order_history")

    return render(
        request,
        "orders/checkout.html",
        {
            "cart": cart,
            "items": items,
        },
    )


@login_required
def order_history(request):

    orders = Order.objects.filter(
        user=request.user
    ).prefetch_related("items__product")

    return render(
        request,
        "orders/order_history.html",
        {"orders": orders},
    )
