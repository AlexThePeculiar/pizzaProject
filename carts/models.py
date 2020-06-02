from django.db import models

# Create your models here.
from pizzaApp.models import Pizzas

class CartItem(models.Model):
    cart = models.ForeignKey('Cart', null=True, blank=True, on_delete=models.DO_NOTHING)
    pizzas = models.ForeignKey('pizzaApp.Pizzas', on_delete=models.DO_NOTHING)
    quantity = models.IntegerField(default=0)
    line_total = models.FloatField(null=True, blank=True, default=0.00)
    def __str__(self):
        try:
            return str(self.cart.id)
        except:
            return self.pizzas.item

class Cart(models.Model):
    total = models.FloatField(null=True, blank=True, default=0.00)
    active = models.BooleanField(default=True)

    def __str__(self):
        return "Cart id: %s" % self.id


