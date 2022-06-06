from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True)
    price = models.DecimalField()
    number_in_store = models.IntegerField()
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'
