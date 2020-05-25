from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
# Create your views here.


from .models import Cart
from pizzaApp.models import Pizzas


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
    else:
        context = {'empty': True}

    template = 'carts/cart.html'
    return render(request, template, context)


def update_cart(request, pizza_id):
    # make a new cart or get a cart if it exists in session
    # request.session.set_expiry(86400)
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
    if not pizza in cart.pizzas.all():
        cart.pizzas.add(pizza)
    else:
        cart.pizzas.remove(pizza)

    # count total price
    new_total = 0.00
    for element in cart.pizzas.all():
        new_total += element.price

    request.session['totalprice'] = new_total
    # print(cart.pizzas.count())
    cart.total = new_total
    cart.save()
    return HttpResponseRedirect(reverse('cart'))
