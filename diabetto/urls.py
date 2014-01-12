# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from diabetto import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^product/', include('product.urls')),
    url(r'^$',  views.IndexView.as_view(), name='index'),
)
