from django.db import models

# Create your models here.

CLASS  = [
    ("Premium", "Premium"),
    ("Standard", "Standard"),
    ("Bestseller", "Bestseller"),
    ("Lux", "Lux"),
]

class Mattress(models.Model):
    title = models.CharField(max_length=255, unique=True)
    photo = models.ImageField(upload_to='img', blank=True)
    base = models.CharField(max_length=255, blank=True)
    border = models.CharField(max_length=255, blank=True)
    edge1 = models.CharField(max_length=255, blank=True)
    edge2 = models.CharField(max_length=255, blank=True)
    height = models.IntegerField(null=True, blank=True)
    case = models.CharField(max_length=255)
    guarantee = models.IntegerField()
    lifetime = models.IntegerField(null=True, blank=True)
    load = models.IntegerField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    mclass = models.CharField(max_length=255, choices=CLASS, default='Standard')

    def __str__(self):
        return self.title
