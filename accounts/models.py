from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

# Create your models here.

class CustomUser(AbstractUser):
    age = models.PositiveBigIntegerField(null=True, blank = True)


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), null=True, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=False, blank = False)
    fav_author = models.CharField(max_length=255)

    def __str__(self):
        return str(self.user)