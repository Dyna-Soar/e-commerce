from django.db import models

from users.models import User


class ClientUser(User):
    COUNTRY_CHOICES = [("FR", "France")]

    country = models.CharField(max_length=64, choices=COUNTRY_CHOICES)
    zip_code = models.CharField(max_length=64)
    address = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.username}'


# TODO: add validators for numeric fields
class Card(models.Model):
    CARD_NETWORK_CHOICES = [("V", "Visa"), ("M", "Mastercard")]

    client = models.ForeignKey(ClientUser, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=64)
    card_network = models.CharField(max_length=64, choices=CARD_NETWORK_CHOICES)
    card_number = models.IntegerField(max_length=32)
    card_security_code = models.IntegerField(max_length=4)
    expiration_date = models.CharField(max_length=8)

    def __str__(self):
        return f"{self.client.username} / {self.full_name}'s card"

    def is_valid_card(self):
        pass
