from django.urls import path,include
from pizzaApp import views


urlpatterns = [
    path('', views.fun, name = 'pizzaApp')
]
