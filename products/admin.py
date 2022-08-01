"""
products/admin.py: Admin models for superuser capabilities with models
Category, Product and Review. Based on admin in
Code Institute's Boutique Ado project.
"""

# - - - - - Django Imports - - - - - - - - -
from django.contrib import admin

# - - - - - Internal Imports - - - - - - - - -
from .models import Product, Category, ProductReview


class ProductAdmin(admin.ModelAdmin):
    """
    The Admin product class
    """
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'image',
    )

    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    """
    The Admin category class
    """
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductReview)
