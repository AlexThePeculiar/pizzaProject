from django.urls import path,include
from pizzaApp import views


urlpatterns = [
    path('', views.index, name = 'pizzaApp')
]
