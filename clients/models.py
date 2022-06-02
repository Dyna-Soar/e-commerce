from django.db import models

from users.models import User


class Client(User):
    COUNTRY_CHOICES = ["France"]

    country = models.CharField(choices=COUNTRY_CHOICES)
    zip_code = models.CharField
    address = models.CharField


# TODO: add validators for numeric fields
class Card(models.Model):
    CARD_NETWORK_CHOICES = ["Visa", "Mastercard"]

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    full_name = models.CharField
    card_network = models.CharField(choices=CARD_NETWORK_CHOICES)
    card_number = models.IntegerField
    card_security_code = models.IntegerField
    expiration_date = models.DateField

    def is_valid_card(self):
        pass
