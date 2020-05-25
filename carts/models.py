from django.db import models

# Create your models here.
from pizzaApp.models import Pizzas


class Cart(models.Model):
    pizzas = models.ManyToManyField(Pizzas, null=True, blank=True)
    total = models.FloatField(null=True, blank=True, default=0.00)
    active = models.BooleanField(default=True)

    def __str__(self):
        return "Cart id: %s" % self.id


