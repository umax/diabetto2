# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns('',
    url(r'^create/$', views.DishCreateView.as_view(),
        name='create_dish'),
    url(r'^$', views.DishIndexView.as_view(),
        name='index_dish'),
)