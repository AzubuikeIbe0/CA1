from django.db import models
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.db.models import DateTimeField
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class Photo(models.Model):
    title = models.CharField(max_length=30, default="Photo Title")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(null=False, blank=False)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        default = None,
        on_delete=models.CASCADE,
    )


    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse('photo', args=[str(self.id)])