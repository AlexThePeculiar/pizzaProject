from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .models import Pizzas
from carts.models import Cart, CartItem


from pizzaApp.models import Cheese, Crust, Diameter, Fish, Fruits, Meat, Mushrooms, Sauce, Saucebase, Vegetables
import itertools
from ast import literal_eval
# Create your views here.

def home(request):
    pizzas = Pizzas.objects.all()
    template = 'pizzaApp/home.html'
    context = {
        'pizzas': pizzas,
    }
    return render(request, template, context)

def edit(request, pizza_id):
    if request.method == "POST":
        try:
            the_id = request.session['cart_id']
        except:
            new_cart = Cart()
            new_cart.save()
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
        else:
            cart_item, created = CartItem.objects.get_or_create(cart=cart, pizzas=pizza, changes=str(changed_pizza))
        cart_item.quantity += 1

        #Change
        cart_item.line_total = pizza.price

        request.session['totalprice'] += cart_item.line_total

        cart_item.save()

        return HttpResponseRedirect(reverse("home"))

    else:
        pizza = Pizzas.objects.get(id = pizza_id)
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