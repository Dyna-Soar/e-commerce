from django.db import models

from clients.models import Client

from products.models import Product


class Order(models.Model):
    LEVEL_CHOICES = ["ACCEPTED", "IN_PREPARATION", "SHIPPED", "DELIVERED"]

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    address_to_ship = models.CharField
    level = models.CharField(default="ACCEPTED")
    additional_information = models.TextField

    def ship(self):
        self.level("SHIPPED").update()

    def deliver(self):
        self.level("SHIPPED").update()