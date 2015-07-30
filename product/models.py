# -*- coding: utf-8 -*-

import decimal

from django.db import models
from django.core.urlresolvers import reverse

from category.models import Category

__all__ = (
    'Product',
)

CARBOHYDRATE_UNIT = decimal.Decimal('12.0')


class Product(models.Model):
    name = models.CharField(
        max_length=128,
        unique=True,
        db_index=True,
        error_messages={'unique': u'Продукт с таким названием уже существует'})
    carbohydrates = models.DecimalField(
        default=0,
        max_digits=3,
        decimal_places=1)
    glycemic_index = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, null=True, default=None)

    class Meta:
        ordering = ['name']
        unique_together = ('name', 'category')
        verbose_name = u'Продукт'
        verbose_name_plural = u'продукты'

    def __unicode__(self):
        return u'%s in %s' % (self.name, self.category)

    def get_absolute_url(self):
        return reverse('detail_product', kwargs={'pk': self.pk})

    @property
    def cu_product(self):
        return round(100 * CARBOHYDRATE_UNIT / self.carbohydrates, 1)

    def admin_product_name(self):
        return self.name
    admin_product_name.short_description = u'Название'
