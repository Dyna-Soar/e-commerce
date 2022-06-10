from django.db import models
from clients.models import ClientUser
from products.models import Product


class OrderItem(models.Model):
    client = models.ForeignKey(ClientUser, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL)
    number_items = models.IntegerField()


class Order(models.Model):
    LEVEL_CHOICES = ["ACCEPTED", "IN_PREPARATION", "SHIPPED", "DELIVERED"]

    client = models.ForeignKey(ClientUser, on_delete=models.CASCADE)
    products = models.ManyToManyField(OrderItem)
    address_to_ship = models.CharField()
    level = models.CharField(default="ACCEPTED")
    additional_information = models.TextField(blank=True)

    def ship(self):
        self.level = "SHIPPED"
        self.save()

    def deliver(self):
        self.level = "DELIVERED"
        self.save()

    def __str__(self):
        return f'{self.client.get_full_name}, shipment: {self.level}'
