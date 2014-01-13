# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import (ListView, DetailView, CreateView,
                                  DeleteView, UpdateView)

from diabetto.mixins import AjaxableResponseMixin

from . import models

__all__ = (
    'CategoryIndexView',
    'CategoryDetailView',
    'CategoryCreateView',
    'CategoryDeleteView',
    'CategoryUpdateView',
)


class CategoryIndexView(ListView):
    model = models.Category
    context_object_name = 'categories'
    template_name = 'category/index.html'


class CategoryDetailView(DetailView):
    model = models.Category
    context_object_name = 'category'
    template_name = 'category/detail.html'


class CategoryCreateView(AjaxableResponseMixin, CreateView):
    model = models.Category
    fields = ['name']
    success_url = reverse_lazy('index_category')


class CategoryUpdateView(AjaxableResponseMixin, UpdateView):
    model = models.Category
    fields = ['name']

    def get_success_url(self):
        return reverse('detail_category', kwargs={'pk': self.object.pk})


class CategoryDeleteView(DeleteView):
    model = models.Category
    context_object_name = 'category'
    success_url = reverse_lazy('index_category')

    def get(self, request, *args, **kwargs):
        """
        Calls the delete() method on the fetched object and then
        redirects to the success URL.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)


