from django.contrib import admin

# Register your models here.
from .models import Pizzas, Orders

admin.site.register(Orders)
admin.site.register(Pizzas)