"""
cart/contexts.py: enables the cart contents to be accessed throughout the site.
Credit to Code Institute's Boutique Ado project.
"""

# - - - - - Python Imports - - - - - - - - -
from decimal import Decimal

# - - - - - Django Imports - - - - - - - - -
from django.conf import settings
from django.shortcuts import get_object_or_404

# - - - - - Internal Imports - - - - - - - - -
from products.models import Product


def bag_contents(request):
    """
    Accesses the cart contents.
    Args:
        request (object)
    Returns:
        the cart contents as its context.
    """

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
