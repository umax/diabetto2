# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import (ListView, DetailView, CreateView, DeleteView,
                                  UpdateView)

from diabetto.mixins import AjaxableResponseMixin

from . import models

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


class ProductCreateView(AjaxableResponseMixin, CreateView):
    model = models.Product
    fields = ['name', 'category']

    def get_success_url(self):
        return reverse('detail_category',
                       kwargs={'pk': self.object.category.id})


class ProductUpdateView(AjaxableResponseMixin, UpdateView):
    model = models.Product
    fields = ['name']

    def get_success_url(self):
        return reverse('detail_product', kwargs={'pk': self.object.id})


class ProductDeleteView(DeleteView):
    model = models.Product
    context_object_name = 'product'

    def get(self, request, *args, **kwargs):
        """
        Calls the delete() method on the fetched object and then
        redirects to the success URL.
        """
        self.object = self.get_object()
        success_url = reverse('detail_category',
                              kwargs={'pk': self.object.category.id})
        self.object.delete()
        return HttpResponseRedirect(success_url)


