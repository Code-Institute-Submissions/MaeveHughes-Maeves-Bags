"""
contact/urls.py: urls for the checkout app
"""

# - - - - - Django Imports - - - - - - - - -
from django.urls import path

# - - - - - Internal Imports - - - - - - - - -
from . import views

urlpatterns = [
    path('', views.contact_form, name='contact')
]
