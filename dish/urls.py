# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns('',
    url(r'^$', views.DishIndexView.as_view(),
        name='index_dish'),
)