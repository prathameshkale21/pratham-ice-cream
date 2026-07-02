from django.db import models
from django.utils.text import slugify


# ==========================================
# Feedback Model
# ==========================================

class Feedback(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    desc = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# ==========================================
# Carousel Model
# ==========================================

class Carousel(models.Model):
    title = models.CharField(max_length=200)
    caption = models.TextField()
    image = models.ImageField(upload_to="carousel/")
    active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title


# ==========================================
# Category Model
# ==========================================

class Category(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to="category/")
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


# ==========================================
# Product Model
# ==========================================

class Product(models.Model):

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products"
    )

    name = models.CharField(max_length=250)

    slug = models.SlugField(
        unique=True,
        blank=True
    )

    description = models.TextField()

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    discount_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )

    stock = models.PositiveIntegerField(default=10)

    image = models.ImageField(
        upload_to="products/"
    )

    available = models.BooleanField(default=True)

    featured = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# ==========================================
# Product Gallery
# ==========================================

class ProductImage(models.Model):

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="gallery"
    )

    image = models.ImageField(
        upload_to="products/gallery/"
    )

    def __str__(self):
        return self.product.name