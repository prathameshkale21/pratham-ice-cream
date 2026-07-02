from django.db import models
from django.contrib.auth.models import User
from home.models import Product


class WishlistItem(models.Model):

    user = models.ForeignKey(
        User,
        related_name="wishlist_items",
        on_delete=models.CASCADE
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "product")
        ordering = ["-added_at"]

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"
