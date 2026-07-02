
from django.contrib import admin
from django.utils.html import format_html

from .models import (
    Category,
    Product,
    ProductImage
)


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        'preview',
        'name',
    )

    search_fields = (
        'name',
    )

    def preview(self, obj):

        return format_html(
            '<img src="{}" width="80" style="border-radius:8px;">',
            obj.image.url
        )

    preview.short_description = "Image"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        'preview',
        'name',
        'category',
        'price',
        'discount_price',
        'stock',
        'featured',
        'available',
    )

    list_editable = (
        'price',
        'discount_price',
        'stock',
        'featured',
        'available',
    )

    search_fields = (
        'name',
    )

    list_filter = (
        'category',
        'featured',
        'available',
    )

    prepopulated_fields = {
        'slug': ('name',)
    }

    inlines = [
        ProductImageInline
    ]

    def preview(self, obj):

        return format_html(
            '<img src="{}" width="90">',
            obj.image.url
        )

    preview.short_description = "Image"