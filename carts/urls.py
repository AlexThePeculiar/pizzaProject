from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from carts import views

urlpatterns = [
    path('', views.view, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    re_path(r'^(?P<id>\d+)/$', views.remove_from_cart, name='remove_from_cart'),
    re_path(r'^(?P<pizza_id>[\w-]+)/$', views.add_to_cart, name='add_to_cart'),
    # path('test', views.home, name='home')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)