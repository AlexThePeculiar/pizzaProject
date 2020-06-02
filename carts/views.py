from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
# Create your views here.


from .models import Cart, CartItem
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
        print(request.POST)

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

    cart_item = CartItem.objects.create(cart=cart, pizzas=pizza)

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