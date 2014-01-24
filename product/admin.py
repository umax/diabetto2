# -*- coding: utf-8 -*-

from django.contrib import admin
from product.models import Product


class ProductAdmin(admin.ModelAdmin):
    view_on_site = False
    list_display = ('admin_product_name',)


admin.site.register(Product, ProductAdmin)
