from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Restaurant(models.Model):
    class TypeChoices(models.TextChoices):
        FASTFOOD = 'FF', 'FastFood'
        INDIAN = 'IN', 'Indian'
        PAKISTANI = 'PK', 'Pakistani'
        ITALIAN = 'IT', 'Italian'
        CHINESE = 'CH', 'Chinese'
        GREEK = 'GR', 'Greek'
        MEXICAN = 'MX', 'Mexican'
        OTHER = 'OT', 'Other'

    name = models.CharField(max_length=100)
    website = models.URLField(default='')
    date_opened = models.DateField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    restaurant_type = models.CharField(choices=TypeChoices.choices, max_length=2)

    def __str__(self):
        return self.name


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='ratings')
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    def __str__(self):
        return f"Rating: {self.rating}"


class Sale(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.SET_NULL, null=True,related_name='sales')
    income = models.DecimalField(max_digits=9, decimal_places=2)
    datetime = models.DateTimeField()