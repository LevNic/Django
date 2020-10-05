from django.db import models
from django.conf import settings

from mainapp.models import Product

# Create your models here.


class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    add_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Basket'
        verbose_name_plural = 'Baskets'
