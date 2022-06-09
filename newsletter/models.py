from django.db import models
from users.models import User


class Subscriber(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    agree = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.user.username}, agree: {self.agree}'
