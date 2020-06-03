from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

from datetime import datetime, timedelta
import pytz
from .models import Cart, CartItem
from pizzaApp.models import Pizzas, Orders, Cheese, Crust, Diameter, Fish, Fruits, Meat, Mushrooms, Sauce, Saucebase, Vegetables
import json


def view(request):
    # get the cart id or set it to none
    try:
        the_id = request.session['cart_id']
    except:
        the_id = None

    # get the cart by its id, otherwise print Empty message
    if the_id:
        cart = Cart.objects.get(id=the_id)
        context = {'cart': cart}

        new_total = 0.00
        for element in cart.cartitem_set.all():
            line_total = element.pizzas.price * element.quantity
            new_total += line_total

        request.session['totalprice'] = new_total
        # print(cart.pizzas.count())
        cart.total = new_total
        cart.save()
    else:
        context = {'empty': True}

    template = 'carts/cart.html'
    return render(request, template, context)


def remove_from_cart(request, id):
    try:
        the_id = request.session['cart_id']
        cart = Cart.objects.get(id=the_id)
    except:
        return HttpResponseRedirect(reverse("cart"))

    cartitem = CartItem.objects.get(id=id)
    cartitem.delete()
    return HttpResponseRedirect(reverse("cart"))


def add_to_cart(request, pizza_id):
    # make a new cart or get a cart if it exists in session
    # request.session.set_expiry(86400)
    if request.method == 'POST':
        qty = int(request.POST['qty'])

    try:
        the_id = request.session['cart_id']
    except:
        new_cart = Cart()
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        the_id = new_cart.id
    cart = Cart.objects.get(id=the_id)

    # get selected pizza and add in to cart
    try:
        pizza = Pizzas.objects.get(id=pizza_id)
    except Pizzas.DoesNotExist:
        pass

    cart_item, succ = CartItem.objects.get_or_create(cart=cart, pizzas=pizza)

    if cart_item.quantity == 0 and int(qty) == -1:
        cart_item.delete()
    elif int(qty) == 0:
        cart_item.delete()
    else:
        cart_item.quantity += int(qty)
        cart_item.save()

    # count total price
    new_total = 0.00
    for element in cart.cartitem_set.all():
        line_total = element.pizzas.price * element.quantity
        new_total += line_total

    request.session['totalprice'] = new_total
    # print(cart.pizzas.count())
    cart.total = new_total
    cart.save()

    if not abs(int(qty)):
        return HttpResponseRedirect(reverse('cart'))
    else:
        return HttpResponseRedirect(reverse('home'))


def checkout(request):
    if request.method == 'POST':
        name = request.POST['firstName']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        comments = request.POST['comments']
        payment = request.POST['paymentMethod']

    try:
        the_id = request.session['cart_id']
        cart = Cart.objects.get(id=the_id)
    except:
        the_id = None

    new_order = Orders.objects.create()
    new_order.firstname = name
    new_order.phone = phone
    new_order.email = email
    new_order.address = address
    new_order.comments = comments
    new_order.payment = payment
    new_order.price = cart.total

    eu = pytz.timezone('Europe/Minsk')
    now = datetime.now(eu)
    done = now + timedelta(0, 2700)
    now = now.strftime('%Y-%m-%d %H:%M')
    done = done.strftime('%Y-%m-%d %H:%M')
    new_order.clock = now
    new_order.clockfinish = done

    pizzas = ''
    for item in cart.cartitem_set.all():
        pizza_dict = json.loads(item.pizzas.ingredients)
        pizza_dict = decipher(pizza_dict)
        pizzas += str(item.quantity) + 'x - ' + str(pizza_dict) + ' \n'
    print(pizzas)

    new_order.orderitems = pizzas
    new_order.save()

    context = {'id': the_id}
    template = 'carts/checkout.html'

    del request.session['cart_id']
    del request.session['totalprice']

    for cartitem in cart.cartitem_set.all():
        cartitem.delete()
    cart.delete()

    return render(request, template, context)


def decipher(dict):
    for key, value in dict.items():
        if key == 'crust':
            changed = Crust.objects.get(id=value).item
        elif key == 'toppings':
            changed = []
            for topping in dict['toppings']:
                if topping[:3] == 'TME':
                    elem = Meat.objects.get(id=topping).item
                elif topping[:3] == 'TMU':
                    elem = Mushrooms.objects.get(id=topping).item
                elif topping[:3] == 'TFR':
                    elem = Fruits.objects.get(id=topping).item
                elif topping[:3] == 'TFI':
                    elem = Fish.objects.get(id=topping).item
                elif topping[:2] == 'TV':
                    elem = Vegetables.objects.get(id=topping).item
                elif topping[:2] == 'TS':
                    elem = Sauce.objects.get(id=topping).item
                else:
                    elem = Cheese.objects.get(id=topping).item
                changed.append(elem)
        elif key == 'sauceBase':
            changed = Saucebase.objects.get(id=value).item
        else:
            changed = Diameter.objects.get(id=value).item
        dict[key] = changed
    return dict