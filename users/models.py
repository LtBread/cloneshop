from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    delivery_address = models.TextField(blank=True, null=True)

    def save_delete(self):
        self.is_active = False
        self.save()
