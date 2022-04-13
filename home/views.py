"""
home/views.py: Views for home app, rendering the landing page of the site.
"""

# - - - - - Django Imports - - - - - - - - -
from django.shortcuts import render


def index(request):
    """ A view to return the index page """

    context = {}
    return render(request, 'home/index.html', context)
