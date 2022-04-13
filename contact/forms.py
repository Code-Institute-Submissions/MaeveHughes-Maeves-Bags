"""
checkout/forms.py: forms for the contact app.
Most of the code is derived from https://www.youtube.com/watch?v=VOddmV4Xl1g
"""

# - - - - - Django Imports - - - - - - - - -
from django import forms

# - - - - - Internal Imports - - - - - - - - -
from .models import Contact


class ContactForm(forms.ModelForm):
    """Class for Form for User to send a Message"""
    class Meta:
        """Update Class Meta Data"""
        model = Contact
        fields = ('full_name', 'email', 'phone_number', 'message')
