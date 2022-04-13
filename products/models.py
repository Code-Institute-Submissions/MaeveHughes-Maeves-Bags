
"""
products/models.py: Contains the models Category, Product and Review.
Inspired by Code Institute's Boutique Ado project.
"""

# - - - - - Django Imports - - - - - - - - -
from django.db import models


class Category(models.Model):
    """
    The Category model class, with fields for the category name.
    """
    class Meta:
        """
        Category Meta class for returning plural name.
        """
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=250)
    friendly_name = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        # pylint: disable=invalid-str-returned, invalid-name
        return self.name

    def get_friendly_name(self):
        """
        Returns the user readable category name as string.
        Args:
            self (object)
        Returns:
            The category friendly name string
        """
        return self.friendly_name


class Product(models.Model):
    """
    The Product model class, used to generate an instance of a product
    """
    name = models.CharField(max_length=250)
    sku = models.CharField(max_length=254, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    description = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        # pylint: disable=invalid-str-returned, invalid-name
        return self.name
