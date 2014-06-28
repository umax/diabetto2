# -*- coding: utf-8 -*-

from django_assets import Bundle, register


dish_base_js = Bundle(
    'js/underscore.js',
    'dish/js/selectmenu.js',
    'dish/js/statistics.js',
    'dish/js/dish.js',
    filters='jsmin',
    output='dish/js/dish_base_all.js')

dish_update_js = Bundle(
    'js/underscore.js',
    'dish/js/selectmenu.js',
    'dish/js/statistics.js',
    'dish/js/dish.js',
    'dish/js/update.js',
    filters='jsmin',
    output='dish/js/dish_update_all.js')

register('dish_base_js', dish_base_js)
register('dish_update_js', dish_update_js)
