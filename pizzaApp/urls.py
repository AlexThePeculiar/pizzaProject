from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from pizzaApp import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('test', views.home, name='home')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
