from django.db import models
from clients.models import Client
from products.models import Product


class ShoppingCart(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_created = models.DateTimeField


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField
    date_created = models.DateTimeField
    shopping_cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)
