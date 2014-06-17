# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, CreateView, DeleteView, UpdateView

from . import forms
from . import models

from category import models as category_models

__all__ = (
    'ProductDetailView',
    'ProductCreateView',
    'ProductDeleteView',
    'ProductUpdateView',
)


class ProductDetailView(DetailView):
    model = models.Product
    context_object_name = 'product'
    template_name = 'product/detail.html'


class ProductCreateView(CreateView):
    form_class = forms.ProductForm
    template_name = 'product/create.html'

    def get_success_url(self):
        return reverse('detail_category',
                       kwargs={'pk': self.object.category.id})

    def get_context_data(self, **kwargs):
        context = super(ProductCreateView, self).get_context_data(**kwargs)
        category = get_object_or_404(category_models.Category,
                                     pk=self.request.GET['category_id'])

        context['category'] = category
        return context


class ProductUpdateView(UpdateView):
    model = models.Product
    context_object_name = 'product'
    template_name = 'product/update.html'
    fields = ['name', 'carbohydrates', 'glycemic_index']

    def get_success_url(self):
        return reverse('detail_product', kwargs={'pk': self.object.id})


class ProductDeleteView(DeleteView):
    model = models.Product
    context_object_name = 'product'
    template_name = 'product/delete.html'

    def get_success_url(self):
        return reverse('detail_category',
                       kwargs={'pk': self.object.category.id})
