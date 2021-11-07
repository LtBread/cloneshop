from datetime import timedelta

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    age = models.PositiveIntegerField(verbose_name='возраст', default=18)
    delivery_address = models.TextField(blank=True, null=True)

    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(default=(now() + timedelta(hours=48)))

    def save_delete(self):
        self.is_active = False
        self.save()

    def is_activation_key_expired(self):
        if now() <= self.activation_key_expires:
            return False
        else:
            return True
