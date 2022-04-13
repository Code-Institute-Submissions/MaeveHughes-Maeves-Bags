"""
products/forms.py: forms to be used with the product app of the application
Inspired by Code Institute's Boutique Ado project.
"""

# - - - - - Django Imports - - - - - - - - -
from django import forms

# - - - - - Internal Imports - - - - - - - - -
from .widgets import CustomClearableFileInput
from .models import Product, Category


class ProductForm(forms.ModelForm):
    """
    The product form, used to create and edit products by admin users.
    """
    class Meta:
        """
        The defines the Product model.
        """
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()    # pylint: disable=no-member
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        # pylint: disable=unused-variable, invalid-name
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
