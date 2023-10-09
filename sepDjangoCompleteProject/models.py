from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    quantity = models.CharField(max_length=30, blank=False, null=False)
    price = models.CharField(max_length=30, blank=False, null=False)
    description = models.CharField(max_length=30, blank=False, null=False)


def __str__(self):
    return self.name
