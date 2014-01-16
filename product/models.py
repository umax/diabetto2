# -*- coding: utf-8 -*-

from django.db import models
from django.core.urlresolvers import reverse

from category.models import Category

__all__ = (
    'Product',
)


class Product(models.Model):
    name = models.CharField(max_length=128)
    carbohydrates = models.PositiveIntegerField(default=0)
    glycemic_index = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, null=True, default=None)

    class Meta:
        ordering = ['name']
        unique_together = ('name', 'category')

    def get_absolute_url(self):
        return reverse('detail_product', kwargs={'pk': self.pk})
