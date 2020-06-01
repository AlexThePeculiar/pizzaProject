from django.db import models

# Create your models here.
from pizzaApp.models import Pizzas

class CartItem(models.Model):
    pizzas = models.ForeignKey('pizzaApp.Pizzas', on_delete=models.DO_NOTHING)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.pizzas.item

class Cart(models.Model):
    items = models.ManyToManyField(CartItem, null=True, blank=True)
    #pizzas = models.ManyToManyField(Pizzas, null=True, blank=True)
    total = models.FloatField(null=True, blank=True, default=0.00)
    active = models.BooleanField(default=True)

    def __str__(self):
        return "Cart id: %s" % self.id


