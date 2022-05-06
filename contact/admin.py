"""
contact/admin.py: admin models for the checkout app.
Most of the code is derived from https://www.youtube.com/watch?v=VOddmV4Xl1g
"""

# - - - - - Django Imports - - - - - - - - -
from django.contrib import admin

# - - - - - Internal Imports - - - - - - - - -
from .models import NewsletterSubscription, Contact


class NewsletterAdmin(admin.ModelAdmin):
    """Newsletter Admin"""
    model = NewsletterSubscription
    list_display = (
        'email',
    )


admin.site.register(Contact)
admin.site.register(NewsletterSubscription, NewsletterAdmin)
