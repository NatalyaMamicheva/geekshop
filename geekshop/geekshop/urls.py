# from django.conf.urls import url, include
from django.conf.urls import include
from django.contrib import admin
import mainapp.views as mainapp

from django.conf import settings
from django.conf.urls.static import static

from django.urls import path

urlpatterns = [
    path('', mainapp.main, name='main'),
    path('products/', include('mainapp.urls', namespace='products')),
    path('contact/', mainapp.contact, name='contact'),
    path('auth/', include('authapp.urls', namespace='auth')),
    path('basket/', include('basketapp.urls', namespace='basket')),
    path('', include('social_django.urls', namespace='social')),
    path('admin/', include('adminapp.urls', namespace='admin')),
    path('order/', include('ordersapp.urls', namespace='order'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
