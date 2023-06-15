from django.db import models


# Create your models here.
class Pizza(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    active = models.BooleanField(default=True)


class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    CATEGORY_CHOICES = [
        ("premium", "Premium"),
        ("basic", "Basic"),
    ]
    category = models.CharField(max_length=7,choices=CATEGORY_CHOICES)
