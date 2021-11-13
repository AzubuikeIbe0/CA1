from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

# Create your models here.

class CustomUser(AbstractUser):
    age = models.PositiveBigIntegerField(null=True, blank = True)


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), null=True, on_delete=models.CASCADE)
    profile_image = models.ImageField(default='', upload_to='images/', null=True, blank=True)
    date_of_birth = models.DateField(null=False, blank = False, default='')
    fav_author = models.CharField(max_length=255, default='')
    description = models.CharField(max_length=1000, default='')
    hobbies = models.CharField(max_length=50, default='')
    city = models.CharField(max_length=50, default='')
    phone = models.IntegerField(default=0)
    website = models.URLField(default='')

    def __str__(self):
        return str(self.user)