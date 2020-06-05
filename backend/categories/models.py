from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(max_length=300)
    slug = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.name
