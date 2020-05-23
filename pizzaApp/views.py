from django.shortcuts import render
from django.template import loader
from .models import Meat, Crust, Sauce
# Create your views here.
def index(request):
	meats = Meat.objects.all()
	crusts = Crust.objects.all()
	sauces = Sauce.objects.all()
	template = loader.get_template('pizzaApp/page1.html')
	context = {
		'meats': meats,
		'crusts': crusts,
		'sauces': sauces,
	}
	return render(request, "pizzaApp/page1.html", context)
	