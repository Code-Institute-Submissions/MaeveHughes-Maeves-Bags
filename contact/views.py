"""
contact/views.py: views to process an order made on the site.
Most of the code is derived from https://www.youtube.com/watch?v=VOddmV4Xl1g
"""

# - - - - - Django Imports - - - - - - - - - - - - -
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string

# - - - - - Internal Imports - - - - - - - - - - - - -
from .forms import NewsletterForm, ContactForm, NewsletterUnsubscribeForm
from .models import NewsletterSubscription

# pylint: disable=redefined-outer-name, invalid-name
# pylint: disable=using-constant-test, invalid-name
# pylint: disable=no-member


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


def newsletter_register(request):
    """
    A view to get the email address from the NewsletterForm.
    Checks whether the user has already subscribed, and
    redirects them to the page they were on if they have.
    If not a confirm message and email is issued to the
    user.
    """

    url = request.META.get('HTTP_REFERER')
    if request.method == "POST":
        newsletter_form = NewsletterForm(request.POST)
        if newsletter_form.is_valid():
            if (
                NewsletterSubscription.objects.filter(
                    email=request.POST.get("email")).exists()
            ):
                messages.info(
                    request,
                    "This email address is already subscribed to the Tarmachan \
                        newsletter.")
                return HttpResponseRedirect(url)
            else:
                newsletter_form.save()
                messages.success(
                    request,
                    "You are now subscribed to the Tarmachan newsletter. \
                        We have sent an email confirmation to you."
                )
                # Sending email confirmation of subscription
                data = newsletter_form.save()
                subscriber_email = data.email
                subject = render_to_string(
                    'contact/confirmation_emails/'
                    'newsletter_subscription_subject.txt',
                )
                body = render_to_string(
                    'contact/confirmation_emails/'
                    'newsletter_subscription_body.txt',
                    {'data': data}
                )
                send_mail(
                    subject,
                    body,
                    settings.DEFAULT_FROM_EMAIL,
                    [subscriber_email],
                )
                return HttpResponseRedirect(url)
        else:
            messages.error(
                request,
                "Failed to subscribe. Please ensure the email you've entered is \
                    valid"
            )
            return HttpResponseRedirect(url)
    else:
        newsletter_form = NewsletterForm()


def newsletter_unsubscribe(request):
    """Unsubcribe from newsletter"""
    template = 'contact/newsletter_unsubscribe.html'
    if request.method == "POST":
        unsubscribe_form = NewsletterUnsubscribeForm(request.POST)
        if unsubscribe_form.is_valid():
            if (
                NewsletterSubscription.objects.filter(
                    email=request.POST.get("email")).exists()
            ):
                email = request.POST.get('email')
                NewsletterSubscription.objects.filter(
                    email=request.POST.get("email")).delete()
                messages.success(
                    request,
                    f'{email} has been removed from our mailing list.'
                )
                # Email confirmation for newsletter unsubscription
                subject = render_to_string(
                    'contact/confirmation_emails/'
                    'newsletter_unsubscribe_subject.txt'
                )
                body = render_to_string(
                    'contact/confirmation_emails/'
                    'newsletter_unsubscribe_body.txt',
                    {'email': email}
                )
                send_mail(
                    subject,
                    body,
                    settings.DEFAULT_FROM_EMAIL,
                    [email],
                )
                return redirect(reverse('home'))
            else:
                messages.error(
                    request,
                    'Sorry! This email is not in our mailing list.'
                )
        else:
            messages.error(
                    request,
                    "Failed to unsubscribe. Please ensure the email you've entered is \
                    valid"
                )

    unsubscribe_form = NewsletterUnsubscribeForm()

    context = {
        "unsubscribe_form": unsubscribe_form
    }

    return render(request, template, context)
