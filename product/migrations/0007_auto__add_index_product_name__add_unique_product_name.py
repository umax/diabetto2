# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding index on 'Product', fields ['name']
        db.create_index(u'product_product', ['name'])

        # Adding unique constraint on 'Product', fields ['name']
        db.create_unique(u'product_product', ['name'])


    def backwards(self, orm):
        # Removing unique constraint on 'Product', fields ['name']
        db.delete_unique(u'product_product', ['name'])

        # Removing index on 'Product', fields ['name']
        db.delete_index(u'product_product', ['name'])


    models = {
        u'category.category': {
            'Meta': {'ordering': "['name']", 'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        u'product.product': {
            'Meta': {'ordering': "['name']", 'unique_together': "(('name', 'category'),)", 'object_name': 'Product'},
            'carbohydrates': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '3', 'decimal_places': '1'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['category.Category']", 'null': 'True'}),
            'glycemic_index': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128', 'db_index': 'True'})
        }
    }

    complete_apps = ['product']