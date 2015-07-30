# -*- coding: utf-8 -*-

from django.forms import ModelForm
from dish.models import Dish, Component

__all__ = (
    'DishForm',
)


class DishForm(ModelForm):
    class Meta:
        model = Dish
        fields = ['name', 'portions', 'comments', 'technics', 'weight']

    def __init__(self, *args, **kwargs):
        super(DishForm, self).__init__(*args, **kwargs)

        self.fields['name'].error_messages.update({
            'required': u'Название блюда не может быть пустым',
        })

    def _clean_weights(self):
        """
        Extract weights for products from POST data.
        """

        postfix = '_weight'
        weights = {}
        for key, value in self.data.iteritems():
            if key.endswith(postfix):
                product_id, _ = key.split('_')
                try:
                    weights[product_id] = int(value)
                except ValueError:
                    continue

        return weights

    def clean_comments(self):
        return self.cleaned_data.get('comments', '')

    def clean(self):
        cleaned_data = super(DishForm, self).clean()
        cleaned_data['weights'] = self._clean_weights()

        return cleaned_data

    def save_products(self, dish):
        dish.components.clear()

        for product_id, weight in self.cleaned_data['weights'].iteritems():
            Component.objects.create(
                dish=dish,
                weight=weight,
                product_id=product_id)

    def save(self, *args, **kwargs):
        dish = super(DishForm, self).save(*args, **kwargs)
        self.save_products(dish)

        return dish
