"""
cart/urls.py: the urls to connect the cart views with their templates.
"""

# - - - - - Django Imports - - - - - - - - -
from django.urls import path

# - - - - - Internal imports - - - - - - - - -
from . import views

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('add/<item_id>/', views.add_to_bag, name='add_to_bag'),
    path("adjust/<item_id>/", views.adjust_bag, name="adjust_bag"),
    path("remove/<item_id>/", views.remove_from_bag, name="remove_from_bag"),
]
