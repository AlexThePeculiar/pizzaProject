from django.contrib import admin

# Register your models here.
from .models import Pizzas, Orders, Cheese, Crust, Diameter, Fish, Fruits, Meat, Mushrooms, Sauce, Saucebase, Vegetables

admin.site.register(Orders)
admin.site.register(Pizzas)
admin.site.register(Cheese)
admin.site.register(Crust)
admin.site.register(Diameter)
admin.site.register(Fish)
admin.site.register(Fruits)
admin.site.register(Meat)
admin.site.register(Mushrooms)
admin.site.register(Sauce)
admin.site.register(Saucebase)
admin.site.register(Vegetables)