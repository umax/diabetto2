# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns('',
    url(r'^create/$', views.DishCreateView.as_view(),
        name='create_dish'),
    url(r'^(?P<pk>\d+)/update/$', views.DishUpdateView.as_view(),
        name='update_dish'),
    url(r'^(?P<pk>\d+)/delete/$', views.DishDeleteView.as_view(),
        name='delete_dish'),
    url(r'^$', views.DishIndexView.as_view(),
        name='index_dish'),
)
