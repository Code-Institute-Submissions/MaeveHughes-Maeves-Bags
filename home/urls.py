"""
home/urls.py: all urls for the home app.
"""

# - - - - - Django Imports - - - - - - - - - - - - -
from django.urls import path

# - - - - - Internal imports - - - - - - - - -
from . import views

urlpatterns = [
    path('', views.index, name='home')
]
