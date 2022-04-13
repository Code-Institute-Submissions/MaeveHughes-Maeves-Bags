"""
contact/admin.py: admin models for the checkout app.
Most of the code is derived from https://www.youtube.com/watch?v=VOddmV4Xl1g
"""

# - - - - - Django Imports - - - - - - - - -
from django.contrib import admin

# - - - - - Internal Imports - - - - - - - - -
from .models import Contact

admin.site.register(Contact)
