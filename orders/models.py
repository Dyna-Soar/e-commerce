from django.db import models
from clients.models import ClientUser
from products.models import Product


class OrderItem(models.Model):
    client = models.ForeignKey(ClientUser, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    number_items = models.IntegerField()


class Order(models.Model):
    LEVEL_CHOICES = ["ACCEPTED", "IN_PREPARATION", "SHIPPED", "DELIVERED"]

    client = models.ForeignKey(ClientUser, on_delete=models.CASCADE)
    products = models.ManyToManyField(OrderItem, blank=True)
    total_price = models.DecimalField(decimal_places=4, max_digits=16, blank=True)
    address_to_ship = models.CharField(max_length=64)
    level = models.CharField(default="ACCEPTED", max_length=64)
    additional_information = models.TextField(blank=True)

    def calculate_total_price(self):
        total_price = 0
        for product in self.products.all():
            total_price += product.price * product.number_items
        return total_price

    def ship(self):
        self.level = "SHIPPED"
        self.save()

    def deliver(self):
        self.level = "DELIVERED"
        self.save()

    def __str__(self):
        return f'{self.client.get_full_name}, shipment: {self.level}'
