from django.shortcuts import render
from .models import Pizzas
from carts.models import Cart


# Create your views here.

def home(request):
    pizzas = Pizzas.objects.all()
    template = 'pizzaApp/home.html'
    context = {
        'pizzas': pizzas,
    }
    return render(request, template, context)
