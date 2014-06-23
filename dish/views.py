# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView

from . import forms
from . import models as dish_models

from product import models as product_models

__all__ = (
    'DishIndexView',
    'DishCreateView',
    'DishDetailView',
)


class DishIndexView(ListView):
    model = dish_models.Dish
    context_object_name = 'dishes'
    template_name = 'dish/index.html'


class DishCreateView(CreateView):
    form_class = forms.DishForm
    template_name = 'dish/create.html'
    success_url = reverse_lazy('index_dish')

    def get_context_data(self, **kwargs):
        context = super(DishCreateView, self).get_context_data(**kwargs)
        context['products'] = list(product_models.Product.objects.all())

        return context


class DishDetailView(DetailView):
    model = dish_models.Dish
    context_object_name = 'dish'
    template_name = 'dish/detail.html'
