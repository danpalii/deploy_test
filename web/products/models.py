from django.db import models

from slugify import slugify


class Product(models.Model):
    slug = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=1000, decimal_places=2)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, null=True)

class Category(models.Model):
    slug = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
