# -*- coding: utf-8 -*-

from django.db import models
from django.core.urlresolvers import reverse

from product.models import Product

__all__ = (
    'Dish',
    'Component',
)


class Dish(models.Model):
    TECH_BOSCH = 'bosh'
    TECH_PANASONIC = 'panasonic'
    TECH_REDMOND = 'redmond'
    TECH_STOVE = 'stove'
    TECH_BREAD = 'bread'
    TECH_CHOICES = (
        (TECH_BOSCH, u'Духовка'),
        (TECH_REDMOND, u'Скороварка'),
        (TECH_PANASONIC, u'Мультиварка'),
        (TECH_STOVE, u'Плита'),
        (TECH_BREAD, u'Хлебопечка')
    )

    name = models.CharField(
        max_length=128,
        unique=True,
        error_messages={'unique': u'Блюдо с таким названием уже существует'})
    portions = models.PositiveIntegerField(default=2)
    components = models.ManyToManyField(Product, through='Component')
    comments = models.TextField(default='', blank=True)
    technics = models.CharField(
        max_length=20,
        default=TECH_REDMOND,
        choices=TECH_CHOICES)

    class Meta:
        ordering = ['name']
        verbose_name = u'Блюдо'
        verbose_name_plural = u'блюда'

    def __unicode__(self):
        return u'Dish: %s' % self.name

    def get_absolute_url(self):
        return reverse('detail_dish', kwargs={'pk': self.pk})


class Component(models.Model):
    dish = models.ForeignKey(Dish)
    product = models.ForeignKey(Product)
    weight = models.PositiveIntegerField(default=0)

    def __unicode__(self):
        return u'Product: %s, weight: %s' % (self.product.name, self.weight)
