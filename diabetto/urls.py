# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from diabetto import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$',  views.IndexView.as_view(), name='index'),

    url(r'^admin/', include(admin.site.urls)),
)
