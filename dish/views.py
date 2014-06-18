# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView

from . import forms
from . import models

__all__ = (
    'DishIndexView',
    'DishCreateView',
    'DishDetailView',
)


class DishIndexView(ListView):
    model = models.Dish
    context_object_name = 'dishes'
    template_name = 'dish/index.html'


class DishCreateView(CreateView):
    form_class = forms.DishForm
    template_name = 'dish/create.html'
    success_url = reverse_lazy('index_dish')


class DishDetailView(DetailView):
    model = models.Dish
    context_object_name = 'dish'
    template_name = 'dish/detail.html'