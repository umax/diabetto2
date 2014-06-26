# -*- coding: utf-8 -*-

import json

from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from . import forms
from . import models as dish_models

from product import models as product_models

__all__ = (
    'DishIndexView',
    'DishCreateView',
    'DishUpdateView',
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


class DishUpdateView(UpdateView):
    model = dish_models.Dish
    form_class = forms.DishForm
    context_object_name = 'dish'
    template_name = 'dish/update.html'

    def get_all_products(self):
        return product_models.Product.objects.all()

    def get_dish_products(self):
        dish_products = []
        for component in self.get_object().component_set.all():
            dish_products.append({
                'id': component.product.id,
                'name': component.product.name,
                'weight': component.weight
            })

        return dish_products

    def get_context_data(self, **kwargs):
        context = super(DishUpdateView, self).get_context_data(**kwargs)
        context.update({
            'all_products': self.get_all_products(),
            'dish_products': json.dumps(self.get_dish_products()),
        })

        return context

    def get_success_url(self):
        return reverse('update_dish', kwargs={'pk': self.object.id})
