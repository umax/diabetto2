# -*- coding: utf-8 -*-

import json

from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from . import forms
from . import models as dish_models

from product import models as product_models

__all__ = (
    'DishIndexView',
    'DishCreateView',
    'DishUpdateView',
    'DishDeleteView',
)


class DishIndexView(ListView):
    context_object_name = 'dishes'
    template_name = 'dish/index.html'

    def get_queryset(self):
        return dish_models.Dish.objects.all().prefetch_related(
            'component_set__product')


class ProductsMixin(object):
    def get_all_products(self):
        return product_models.Product.objects.all()

    def get_json_all_products(self):
        products = {}
        for product in self.get_all_products():
            products[product.id] = {
                'name': product.name,
                'carbohydrates': float(product.carbohydrates),
            }

        return products

    def get_json_dish_products(self):
        dish_products = []
        for component in self.get_object().component_set.all():
            dish_products.append({
                'id': component.product.id,
                'name': component.product.name,
                'weight': component.weight,
            })

        return dish_products

    def get_context_data(self, **kwargs):
        context = super(ProductsMixin, self).get_context_data(**kwargs)

        context.update({
            'all_products': self.get_all_products(),
            'json_all_products': json.dumps(self.get_json_all_products()),
            'json_dish_products': json.dumps(self.get_json_dish_products()),
        })

        return context


class DishCreateView(ProductsMixin, CreateView):
    form_class = forms.DishForm
    template_name = 'dish/create.html'
    success_url = reverse_lazy('index_dish')

    def get_json_dish_products(self):
        return []


class DishUpdateView(ProductsMixin, UpdateView):
    model = dish_models.Dish
    form_class = forms.DishForm
    context_object_name = 'dish'
    template_name = 'dish/update.html'

    def get_success_url(self):
        return reverse('update_dish', kwargs={'pk': self.object.id})


class DishDeleteView(DeleteView):
    model = dish_models.Dish
    context_object_name = 'dish'
    template_name = 'dish/delete.html'
    success_url = reverse_lazy('index_dish')
