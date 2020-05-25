from django.shortcuts import render

# Create your views here.

from .models import Cart

def view(request):
    cart = Cart.objects.all()[0]
    context = {'cart':cart}
    template = 'carts/cart.html'
    return render(request, template, context)