from django.shortcuts import render
from .models import Product

# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()

    context = {
        'bag_products': products,
    }

    return render(request, 'bag_products/products.html', context)