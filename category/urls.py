# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)/delete/$', views.CategoryDeleteView.as_view(),
        name='delete_category'),
    url(r'^(?P<pk>\d+)/update/$', views.CategoryUpdateView.as_view(),
        name='update_category'),
    url(r'^(?P<pk>\d+)/$', views.CategoryDetailView.as_view(),
        name='detail_category'),
    url(r'^create/$', views.CategoryCreateView.as_view(),
        name='create_category'),
    url(r'^$', views.CategoryIndexView.as_view(),
        name='index_category'),
)