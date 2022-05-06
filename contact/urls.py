"""
contact/urls.py: urls for the checkout app
"""

# - - - - - Django Imports - - - - - - - - -
from django.urls import path

# - - - - - Internal Imports - - - - - - - - -
from . import views

urlpatterns = [
    path('', views.contact_form, name='contact'),
    path(
        'newsletter_register/',
        views.newsletter_register, name='newsletter_register'
    ),
    path(
        'newsletter_unsubscribe/',
        views.newsletter_unsubscribe, name='newsletter_unsubscribe'
    ),
]
