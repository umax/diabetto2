# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)/$', views.ProductDetailView.as_view(),
        name='detail_product'),
    url(r'^create/$', views.ProductCreateView.as_view(),
        name='create_product'),
    url(r'^$', views.ProductIndexView.as_view(),
        name='index_product'),
)