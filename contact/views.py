"""
contact/views.py: views to process an order made on the site.
Most of the code is derived from https://www.youtube.com/watch?v=VOddmV4Xl1g
"""

# - - - - - Django Imports - - - - - - - - - - - - -
from django.shortcuts import render, redirect
from django.contrib import messages

# - - - - - Internal Imports - - - - - - - - - - - - -
from .forms import ContactForm

# pylint: disable=redefined-outer-name, invalid-name
# pylint: disable=using-constant-test, invalid-name


def contact_form(request):
    """
    A view that returns the contact page
    """
    contact_form = ContactForm()

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid:
            contact_form.save()
            messages.success(request, 'Thank you for contacting us!\
                             We will get back at you in the next 24 hours.')
            return redirect('contact')

    template = 'contact/contact.html'

    context = {
        'contact_form': contact_form,
        'on_profile_page': True
    }

    return render(request, template, context)
