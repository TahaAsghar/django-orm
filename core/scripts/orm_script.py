from django.contrib.auth.models import User
from django.utils import timezone
from django.db import connection
from core.models import Restaurant, Rating, Sale
from pprint import pprint


def run():
    """ creating a sale for a single restaurant """
    Sale.objects.create(
        restaurant=Restaurant.objects.first(),
        income=33.4,
        datetime=timezone.now()
    )

    """ get restaurant ratings """
    restaurant = Restaurant.objects.first()
    print(restaurant.ratings.all())

    """ create a restaurant """
    # restaurant = Restaurant.objects.first()
    # user = User.objects.first()
    # Rating.objects.create(
    #     user=user,
    #     restaurant=restaurant,
    #     rating=3
    # )

    # pprint(connection.queries)

