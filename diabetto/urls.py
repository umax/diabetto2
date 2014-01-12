# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from diabetto import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    url(r'products/(?P<pk>\d+)/$', views.ProductDetailView.as_view(),
        name='detail_product'),
    url(r'products/create/$', views.ProductCreateView.as_view(),
        name='create_product'),
    url(r'products/$', views.ProductIndexView.as_view(),
        name='index_product'),

    url(r'^$',  views.IndexView.as_view(), name='index'),
)
