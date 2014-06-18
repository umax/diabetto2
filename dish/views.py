# -*- coding: utf-8 -*-

from django.views.generic import ListView

from . import models

__all__ = (
    'DishIndexView',
)


class DishIndexView(ListView):
    model = models.Dish
    context_object_name = 'dishes'
    template_name = 'dish/index.html'
