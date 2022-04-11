""" Testing code adapted from Code Institute BoutiqueAdo project """
from django.test import TestCase
from .forms import ReviewForm


class TestReviewForm(TestCase):
    """ Tests for review form """
    def test_title_required(self):
        """ Test title field is required """
        form = ReviewForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(
                         form.errors['title'][0],
                         'This field is required.'
        )

    def test_review_content_is_required(self):
        """ Test review content field is required """
        form = ReviewForm({'review_content': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('review_content', form.errors.keys())
        self.assertEqual(
                         form.errors['review_content'][0],
                         'This field is required.'
        )

    def test_rating_is_required(self):
        """ Test rating field is required """
        form = ReviewForm({'rating': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('rating', form.errors.keys())
        self.assertEqual(
                         form.errors['rating'][0],
                         'This field is required.'
        )