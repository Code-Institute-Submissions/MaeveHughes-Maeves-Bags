"""
profiles/views.py: views for profile app.
Credit to Code Institute for profile and order_history views.
"""

# - - - - - Django Imports - - - - - - - - -
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# - - - - - Internal Imports - - - - - - - - -
from checkout.models import Order
from .models import UserProfile
from .forms import UserProfileForm

# pylint: disable=no-member


@login_required
def profile(request):
    """ Display the user's profile. """
    # pylint: disable=redefined-outer-name
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(
                request, 'Update failed. Please ensure the form is valid.'
                )
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    """
    Returns the users order history.
    Args:
        request (the request object)
        order_number (the order instance)
    Returns:
        the order confirmation page (template and context)
    """
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
