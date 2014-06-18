# -*- coding: utf-8 -*-

from django.forms import ModelForm
from dish.models import Dish

__all__ = (
    'DishForm',
)


class DishForm(ModelForm):
    class Meta:
        model = Dish
        fields = ['name', 'portions']

    def __init__(self, *args, **kwargs):
        super(DishForm, self).__init__(*args, **kwargs)

        self.fields['name'].error_messages.update({
            'required': u'Название блюда не может быть пустым',
        })
