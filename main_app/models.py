from django.db import models
from django.urls import reverse

# Create your models here.


class Finch(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    location = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)

# to return a readable object


def __str__(self):
    return self.name


def get_absolute_url(self):
    return reverse('detail', kwargs={'finch_id': self.id})  # /cats/3 ex
