from django.db import models
from categories.models import Category

def product_photo_path(instance, filename):
    return 'products/{}/{}/{}'.format(instance.category, instance.name, filename)


class Product(models.Model):
    name = models.CharField(max_length=250, unique=True, blank=False)
    photo = models.ImageField(upload_to=product_photo_path)
    category = models.ForeignKey(Category, to_field='name', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    description = models.TextField(blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    in_stock = models.BooleanField(default=False)
    trending = models.BooleanField(default=False)

    def __str__(self):
        return self.name