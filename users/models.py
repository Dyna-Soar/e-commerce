from django.db import models


class User(models.Model):
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=256)
    email = models.EmailField
    is_team = models.BooleanField(default=False)
