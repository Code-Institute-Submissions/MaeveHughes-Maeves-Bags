"""
contact/models.py: Models within the contact app.
Most of the code is derived from https://www.youtube.com/watch?v=VOddmV4Xl1g
"""

# - - - - - Django Imports - - - - - - - - -
from django.db import models


class Contact(models.Model):
    """
    Class for a Message from Signed In User
    """
    full_name = models.CharField(max_length=120, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    message = models.TextField(null=False, blank=False)

    def __str__(self):
        # pylint: disable=invalid-str-returned, invalid-name
        return self.full_name
