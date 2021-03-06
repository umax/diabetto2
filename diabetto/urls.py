# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from diabetto import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^category/', include('category.urls')),
    url(r'^product/', include('product.urls')),
    url(r'^dish/', include('dish.urls')),
    url(r'^$',  views.IndexView.as_view(), name='index'),
)
