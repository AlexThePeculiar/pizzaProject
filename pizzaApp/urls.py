from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from pizzaApp import views

urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'^edit/(?P<pizza_id>[\w-]+)/$', views.edit, name='edit'),
    # path('test', views.home, name='home')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
