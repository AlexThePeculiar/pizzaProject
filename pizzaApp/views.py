from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .models import Pizzas
from carts.models import Cart, CartItem

from pizzaApp.models import Cheese, Crust, Diameter, Fish, Fruits, Meat, Mushrooms, Sauce, Saucebase, Vegetables
from carts.views import output
import itertools
from ast import literal_eval


# Create your views here.

def home(request):
    pizzas = Pizzas.objects.all()

    items = []
    for pizza in pizzas:
        items.append([pizza, output(literal_eval(pizza.ingredients))])

    template = 'pizzaApp/home.html'
    context = {
        'pizzas': items,
    }
    return render(request, template, context)


def edit(request, pizza_id):
    if request.method == "POST":
        try:
            the_id = request.session['cart_id']
        except:
            new_cart = Cart()
            new_cart.save()
            request.session['totalprice'] = 0
            request.session['cart_id'] = new_cart.id
            the_id = new_cart.id
        cart = Cart.objects.get(id=the_id)
        pizza = Pizzas.objects.get(id=pizza_id)

        changed_pizza = {'crust': request.POST['crust'], 'toppings': sorted(request.POST.getlist('toppings')),
                         'sauceBase': request.POST['sauceBase'], 'diameter': request.POST['diameter']}

        ingr = literal_eval(pizza.ingredients)
        ingr['toppings'] = sorted(ingr['toppings'])
        if ingr == changed_pizza:
            cart_item, created = CartItem.objects.get_or_create(cart=cart, pizzas=pizza)
            cart_item.line_total = pizza.price
        else:
            cart_item, created = CartItem.objects.get_or_create(cart=cart, pizzas=pizza, changes=str(changed_pizza))
            price = 5
            for topping in changed_pizza['toppings']:
                if topping[:3] == 'TME':
                    elem = Meat.objects.get(id=topping).price
                elif topping[:3] == 'TMU':
                    elem = Mushrooms.objects.get(id=topping).price
                elif topping[:3] == 'TFR':
                    elem = Fruits.objects.get(id=topping).price
                elif topping[:3] == 'TFI':
                    elem = Fish.objects.get(id=topping).price
                elif topping[:2] == 'TV':
                    elem = Vegetables.objects.get(id=topping).price
                elif topping[:2] == 'TS':
                    elem = Sauce.objects.get(id=topping).price
                else:
                    elem = Cheese.objects.get(id=topping).price
                price += elem
            price += Diameter.objects.get(id=changed_pizza['diameter']).price
            cart_item.price_changed = round(price, 2)
            cart_item.line_total = cart_item.price_changed

        cart_item.quantity += 1

        request.session['totalprice'] += cart_item.line_total
        cart_item.save()

        return HttpResponseRedirect(reverse("home"))

    else:
        pizza = Pizzas.objects.get(id=pizza_id)
        initial_toppings = literal_eval(pizza.ingredients)['toppings']
        initial_crust = literal_eval(pizza.ingredients)['crust']
        initial_sauceBase = literal_eval(pizza.ingredients)['sauceBase']
        initial_diameter = literal_eval(pizza.ingredients)['diameter']

        cheeses = Cheese.objects.all()
        crusts = Crust.objects.all()
        diameters = Diameter.objects.all()
        fish = Fish.objects.all()
        fruits = Fruits.objects.all()
        meats = Meat.objects.all()
        mushrooms = Mushrooms.objects.all()
        sauces = Sauce.objects.all()
        sauceBases = Saucebase.objects.all()
        vegetables = Vegetables.objects.all()

        new_toppings = list(itertools.zip_longest(cheeses, fish, fruits, meats, mushrooms, sauces, vegetables))

        context = {
            'pizza_id': pizza_id,
            'toppings': new_toppings,
            'crusts': crusts,
            'diameters': diameters,
            'sauceBases': sauceBases,
            'initial_toppings': initial_toppings,
            'initial_crust': initial_crust,
            'initial_sauceBase': initial_sauceBase,
            'initial_diameter': initial_diameter,
        }
        template = 'pizzaApp/edit.html'
        return render(request, template, context)
