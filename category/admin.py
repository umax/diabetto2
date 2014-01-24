# -*- coding: utf-8 -*-

from django.contrib import admin
from category.models import Category


class CategoryAdmin(admin.ModelAdmin):
    view_on_site = False
    list_display = ('admin_category_name', 'admin_products_count')


admin.site.register(Category, CategoryAdmin)
