# -*- coding: utf-8 -*-

from django.db import models
from django.core.urlresolvers import reverse

from category.models import Category

__all__ = (
    'Product',
)

CARBOHYDRATE_UNIT = 12.0

class Product(models.Model):
    name = models.CharField(max_length=128)
    carbohydrates = models.PositiveIntegerField(default=0)
    glycemic_index = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, null=True, default=None)

    class Meta:
        ordering = ['name']
        unique_together = ('name', 'category')
        verbose_name = u'Продукт'
        verbose_name_plural = u'продукты'

    def get_absolute_url(self):
        return reverse('detail_product', kwargs={'pk': self.pk})

    @property
    def cu_product(self):
        return '%.2f' % (100 * CARBOHYDRATE_UNIT / self.carbohydrates)

    def admin_product_name(self):
        return self.name
    admin_product_name.short_description = u'Название'
