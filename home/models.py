from django.db import models

class student (models.Model):
    name = models.CharField()
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField(null= True, blank=True)
    image = models.ImageField()
    file = models.FileField()

class Product (models.Model):
    pass
