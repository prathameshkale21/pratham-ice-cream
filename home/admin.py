from django.contrib import admin
from .models import (
    Feedback,
    Carousel,
    Category,
    Product,
    ProductImage,
)

admin.site.site_header = "🍦 Pratham Ice Cream — Admin"
admin.site.site_title = "Pratham Ice Cream Admin"
admin.site.index_title = "Dashboard"


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "phone",
        "date",
    )

    search_fields = (
        "name",
        "email",
    )


@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "active",
        "order",
    )

    list_editable = (
        "active",
        "order",
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
    )


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "category",
        "price",
        "discount_price",
        "stock",
        "available",
        "featured",
    )

    list_filter = (
        "category",
        "available",
        "featured",
    )

    search_fields = (
        "name",
        "description",
    )

    prepopulated_fields = {
        "slug": ("name",)
    }

    inlines = [
        ProductImageInline
    ]