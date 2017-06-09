__author__ = 'oleh'

from django.conf.urls import url

import views
from django.contrib.auth.views import login

urlpatterns = [
    # ex: /mobiles/
    url(r'^$', views.index, name='index'),
    url(r'^login/$', login),
    # url(r'^logout/$', 'django.contrib.auth.views.logout'),


    url(r'^(?P<mobile_id>\d+)/$', views.detail, name='detail'),
    url(r'^card/$', views.card, name='results'),

    url(r'^card/remove/(?P<mobile_id>\d+)/', views.remove, name='results'),

    url(r'^(?P<mobile_id>\d+)/buy/$', views.buy, name='buy'),
]