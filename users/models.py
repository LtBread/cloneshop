from datetime import timedelta

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from django.dispatch import receiver
from django.db.models.signals import post_save


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True, null=True)
    # birthday = models.DateField(blank=True, null=True)
    # age = models.PositiveIntegerField(verbose_name='возраст', default=18)
    # delivery_address = models.TextField(blank=True, null=True)

    activation_key = models.CharField(max_length=128, blank=True)

    # activation_key_expires = models.DateTimeField(default=(now() + timedelta(hours=48)))

    def save_delete(self):
        self.is_active = False
        self.save()

    # def is_activation_key_expired(self):
    #     if now() <= self.activation_key_expires:
    #         return False
    #     else:
    #         return True

    def is_activation_key_expired(self):
        return now() - self.date_joined > timedelta(hours=48)


class UserProfile(models.Model):
    MALE = 'M'
    FEMALE = 'W'
    GENDER_CHOICES = ((MALE, 'М'), (FEMALE, 'Ж'))

    user = models.OneToOneField(
        User,
        unique=True,
        null=False,
        db_index=True,
        on_delete=models.CASCADE
    )

    age = models.PositiveIntegerField(verbose_name='возраст', default=18)
    tagline = models.CharField(verbose_name='теги', max_length=128, blank=True)
    about_me = models.TextField(verbose_name='о себе', max_length=512, blank=True)
    gender = models.CharField(verbose_name='пол', max_length=1, choices=GENDER_CHOICES, blank=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.userprofile.save()
