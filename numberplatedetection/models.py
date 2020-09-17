from django.db import models
from django.utils.timezone import now

# Create your models here.


class Pictures(models.Model):
    location = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    created_date = models.DateTimeField(auto_now_add=True)


class Challan(models.Model):
    numberplate = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    mobilenumber = models.BigIntegerField()
    objects = models.Manager()


    def __str__(self):
        return self.numberplate

