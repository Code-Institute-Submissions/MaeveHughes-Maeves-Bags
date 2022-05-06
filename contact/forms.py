"""
checkout/forms.py: forms for the contact app.
Most of the code is derived from https://www.youtube.com/watch?v=VOddmV4Xl1g
"""

# - - - - - Django Imports - - - - - - - - -
from django import forms

# - - - - - Internal Imports - - - - - - - - -
from .models import NewsletterSubscription, Contact


class NewsletterForm(forms.ModelForm):
    """
    Create a form for any user to subscribe to the company
    newsletter
    """

    class Meta:
        """Newsletter Subscription"""
        model = NewsletterSubscription
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].widget.attrs["placeholder"] = "Email *"
        self.fields["email"].widget.attrs['class'] = "subscribe-input"
        # updates the input id to a unique id for the page
        self.fields["email"].widget.attrs['id'] = "newsletter-email"
        self.fields["email"].label = False


class NewsletterUnsubscribeForm(forms.ModelForm):
    """
    Create a form for any user to unsubscribe to the company
    newsletter
    """

    class Meta:
        """Newsletter Unsubscribe"""
        model = NewsletterSubscription
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["email"].widget.attrs["placeholder"] = "Email *"
        self.fields["email"].widget.attrs['class'] = "product-style-input"
        self.fields["email"].label = False


class ContactForm(forms.ModelForm):
    """Class for Form for User to send a Message"""
    class Meta:
        """Update Class Meta Data"""
        model = Contact
        fields = ('full_name', 'email', 'phone_number', 'message')
