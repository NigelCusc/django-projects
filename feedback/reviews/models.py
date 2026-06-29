from django.core.validators import MaxValueValidator, MinLengthValidator, MinValueValidator
from django.db import models

class Review(models.Model):
    user_name = models.CharField(max_length=100, validators=[MinLengthValidator(2)])
    review_text = models.TextField(max_length=200, validators=[MinLengthValidator(10)])
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f"{self.user_name} - ({self.rating})"
