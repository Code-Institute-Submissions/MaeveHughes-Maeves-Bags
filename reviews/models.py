from django.db import models

from profiles.models import UserProfile
from products.models import Product


class Review(models.Model):

    RATING = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    review_content = models.TextField()
    rating = models.IntegerField(choices=RATING)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        """ to show most recent reviews first """
        ordering = ['-date_created']

    def __str__(self):
        return self.title