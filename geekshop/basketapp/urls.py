# from django.conf.urls import url

import basketapp.views as basketapp
from django.urls import re_path

app_name="basketapp"

urlpatterns = [
    re_path(r'^$', basketapp.basket, name='view'),
    re_path(r'^add/(?P<pk>\d+)/$', basketapp.basket_add, name='add'),
    re_path(r'^remove/(?P<pk>\d+)/$', basketapp.basket_remove, name='remove'),

    re_path(r'^edit/(?P<pk>\d+)/(?P<quantity>\d+)/$', basketapp.basket_edit, name='edit'),
]

    