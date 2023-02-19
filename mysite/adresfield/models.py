from django.db import models

# Create your models here.


class Addres(models.Model):
    street_from = models.CharField('From', max_length=70)
    street_to = models.CharField('To', max_length=70)
    name = models.CharField('Name', max_length=50)
    phone = models.CharField('Phone', max_length=12)


    class Meta:
        verbose_name = "Boocked trip"
        verbose_name_plural = "Trips"
