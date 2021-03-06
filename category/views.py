# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse_lazy
from django.views.generic import (ListView, DetailView, CreateView,
                                  DeleteView, UpdateView)

from . import forms
from . import models

__all__ = (
    'CategoryIndexView',
    'CategoryDetailView',
    'CategoryCreateView',
    'CategoryDeleteView',
    'CategoryUpdateView',
)


class CategoryIndexView(ListView):
    context_object_name = 'categories'
    template_name = 'category/index.html'

    def get_queryset(self):
        return models.Category.objects.all().prefetch_related('products')


class CategoryDetailView(DetailView):
    context_object_name = 'category'
    template_name = 'category/detail.html'

    def get_queryset(self):
        return models.Category.objects.all().prefetch_related('products')


class CategoryCreateView(CreateView):
    form_class = forms.CategoryForm
    template_name = 'category/create.html'
    success_url = reverse_lazy('index_category')


class CategoryUpdateView(UpdateView):
    model = models.Category
    form_class = forms.CategoryForm
    context_object_name = 'category'
    template_name = 'category/update.html'
    success_url = reverse_lazy('index_category')


class CategoryDeleteView(DeleteView):
    model = models.Category
    context_object_name = 'category'
    template_name = 'category/delete.html'
    success_url = reverse_lazy('index_category')
