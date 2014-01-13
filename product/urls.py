# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)/delete/$', views.ProductDeleteView.as_view(),
        name='delete_product'),
    url(r'^(?P<pk>\d+)/update/$', views.ProductUpdateView.as_view(),
        name='update_product'),
    url(r'^(?P<pk>\d+)/$', views.ProductDetailView.as_view(),
        name='detail_product'),
    url(r'^create/$', views.ProductCreateView.as_view(),
        name='create_product'),
)