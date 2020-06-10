from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse
from pizzaProject.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
# Create your views here.

from datetime import datetime, timedelta
import pytz
from .models import Cart, CartItem
from pizzaApp.models import Pizzas, Orders, Cheese, Crust, Diameter, Fish, Fruits, Meat, Mushrooms, Sauce, Saucebase, \
    Vegetables
from ast import literal_eval


def view(request):
    # get the cart id or set it to none
    try:
        the_id = request.session['cart_id']
    except:
        the_id = None

    # get the cart by its id, otherwise print Empty message
    if the_id:
        cart = Cart.objects.get(id=the_id)

        request.session['totalprice'] = cartTotal(cart)
        # print(cart.pizzas.count())

        items = []
        for item in cart.cartitem_set.all():
            if item.changes is None:
                items.append([item, output(literal_eval(item.pizzas.ingredients))])
            else:
                items.append([item, output(literal_eval(item.changes))])
        context = {'items': items, 'cart': cart}

    else:
        context = {'empty': True}

    template = 'carts/cart.html'
    return render(request, template, context)


def alter_items_cart(request):
    if request.method == 'POST':
        qty = int(request.POST['qty'])
        item_id = int(request.POST['item_id'])
    print(request.POST)
    try:
        the_id = request.session['cart_id']
        cart = Cart.objects.get(id=the_id)
    except:
        return HttpResponseRedirect(reverse("cart"))

    cartitem = CartItem.objects.get(id=item_id)
    if qty == 0:
        cartitem.delete()
    elif qty == -1 and cartitem.quantity == 1:
        cartitem.delete()
    else:
        cartitem.quantity += qty
        cartitem.save()

    total_price = cartTotal(cart)
    request.session['totalprice'] = total_price
    return JsonResponse({'total_quantity': cartitem.quantity, 'total_price': total_price})


def add_to_cart(request):
    # make a new cart or get a cart if it exists in session
    # request.session.set_expiry(86400)
    if request.method == 'POST':
        qty = int(request.POST['qty'])
        pizza_id = request.POST['pizza_id']

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

    cart_item, succ = CartItem.objects.get_or_create(cart=cart, pizzas=pizza, changes=None)

    cart_item.quantity += int(qty)
    cart_item.save()

    # count total price
    new_total = 0.00
    for element in cart.cartitem_set.all():
        line_total = element.pizzas.price * element.quantity
        new_total += line_total

    cart_item.line_total = line_total
    cart_item.save()
    request.session['totalprice'] = new_total
    # print(cart.pizzas.count())

    cart.total = new_total
    cart.save()
    return JsonResponse({'total_price': round(new_total, 2)})


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
    new_order.price = round(cart.total, 2)

    eu = pytz.timezone('Europe/Minsk')
    now = datetime.now(eu)
    done = now + timedelta(0, 2700)
    now = now.strftime('%Y-%m-%d %H:%M')
    done = done.strftime('%Y-%m-%d %H:%M')
    new_order.clock = now
    new_order.clockfinish = done

    pizzas = ''
    for item in cart.cartitem_set.all():
        if item.changes is None:
            pizza_dict = literal_eval(item.pizzas.ingredients)
        else:
            pizza_dict = literal_eval(item.changes)

        pizza_dict = decipher(pizza_dict)
        pizzas += str(item.quantity) + 'x - ' + str(pizza_dict) + ' \n'

    new_order.orderitems = pizzas
    new_order.save()

    template = 'carts/checkout.html'
    context = {'id': the_id, 'name': name}

    if email is not '':
        sendmail(name, email, comments, now, cart)

    del request.session['cart_id']
    del request.session['totalprice']

    for cartitem in cart.cartitem_set.all():
        cartitem.delete()
    cart.delete()

    return render(request, template, context)


def cartTotal(cart):
    new_total = 0.00
    for element in cart.cartitem_set.all():
        if element.changes is None:
            line_total = element.pizzas.price * element.quantity
        else:
            line_total = element.price_changed * element.quantity
        new_total += line_total
        cart.total = new_total
        cart.save()
    return new_total


def decipher(dicty):
    for key, value in dicty.items():
        if key == 'crust':
            changed = Crust.objects.get(id=value).item
        elif key == 'toppings':
            changed = []
            for topping in dicty['toppings']:
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
        dicty[key] = changed
    return dicty


def output(dicty):
    crust = Crust.objects.get(id=dicty['crust']).item
    diameter = Diameter.objects.get(id=dicty['diameter']).item
    sauceBase = Saucebase.objects.get(id=dicty['sauceBase']).item
    general = str(diameter) + ' см, ' + crust + ' тесто, ' + sauceBase + ' соус'

    toppings = ''
    i = 1
    for topping in dicty['toppings']:
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

        if i < len(dicty['toppings']):
            toppings += elem + ', '
        else:
            toppings += elem
        i += 1

    return [general, toppings]


def sendmail(name, email, comments, time, cart):
    items = []
    for item in cart.cartitem_set.all():
        if item.changes is None:
            items.append([item, output(literal_eval(item.pizzas.ingredients))])
        else:
            items.append([item, output(literal_eval(item.changes))])

    text = 'Дорогой товарищ ' + name + '! Спасибо, что оформили заказ на нашем сайте! ' + 'Ваш заказ был оформлен ' \
           + time + ' под номером №' + str(cart.id) + '. Ваш заказ на сумму ' + str(
        round(cart.total, 2)) + '0' + ' рублей:\n'

    for item in items:
        if item[0].changes is None:
            name = item[0].pizzas.item
        else:
            name = item[0].pizzas.item + ' (изменённая)'
        text += name + ' x' + str(item[0].quantity) + ':\n        ' + item[1][0] + '\n        ' + item[1][1] + '\n'

    if comments is not '':
        text += '\nВаши комментарий к заказу: ' + comments + '\n'

    text += '\nДа хранит вас Владимир Ильич Ленин!\nСлава КПСС и Советскому Союзу!'
    subject = 'Заказ №' + str(cart.id)
    send_mail(subject, text, EMAIL_HOST_USER, [email], fail_silently=False)
