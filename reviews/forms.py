from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """ ReviewForm to allow users to add reviews """
    class Meta:
        model = Review
        fields = ('title', 'review_content', 'rating')

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.fields['review_content'].label = "Review"