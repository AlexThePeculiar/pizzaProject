from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from carts import views

urlpatterns = [
    path('', views.view, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('alter-item/', views.alter_items_cart, name='alter_items_cart'),
    path('add-item/', views.add_to_cart, name='add_to_cart'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)