import os

from django.core.management.base import BaseCommand
from home.models import Category, Product


class Command(BaseCommand):
    """
    Deletes ALL categories and products (and anything that cascades from
    them — product images, cart items, wishlist items, order items).

    Only runs when the CLEAR_CATALOG environment variable is set to
    "true". This is intentional: it's meant to be used ONCE, right after
    switching to Cloudinary, to wipe out products/categories that were
    uploaded before persistent storage was set up. After running it once,
    remove or set CLEAR_CATALOG back to "false" so it doesn't wipe your
    real catalog on a future deploy.
    """

    help = "One-time reset: deletes all categories and products."

    def handle(self, *args, **options):

        if os.environ.get("CLEAR_CATALOG", "false").lower() != "true":
            self.stdout.write(
                "CLEAR_CATALOG is not set to 'true' — skipping catalog reset."
            )
            return

        product_count = Product.objects.count()
        category_count = Category.objects.count()

        Product.objects.all().delete()
        Category.objects.all().delete()

        self.stdout.write(
            self.style.WARNING(
                f"Cleared catalog: deleted {product_count} product(s) and "
                f"{category_count} categorie(s)."
            )
        )
