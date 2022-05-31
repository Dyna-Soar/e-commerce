from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_length=16)

    def __str__(self):
        return f'{self.name}'
