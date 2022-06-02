from django.db import models


# Add validator for numerical fields
class Product(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True)
    price = models.DecimalField
    available_number = models.IntegerField
    date_created = models.DateTimeField
    date_updated = models.DateTimeField(default=date_created)

    def __str__(self):
        return f'{self.name}'
