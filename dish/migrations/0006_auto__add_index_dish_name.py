# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding index on 'Dish', fields ['name']
        db.create_index(u'dish_dish', ['name'])


    def backwards(self, orm):
        # Removing index on 'Dish', fields ['name']
        db.delete_index(u'dish_dish', ['name'])


    models = {
        u'category.category': {
            'Meta': {'ordering': "['name']", 'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        u'dish.component': {
            'Meta': {'object_name': 'Component'},
            'dish': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dish.Dish']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['product.Product']"}),
            'weight': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        u'dish.dish': {
            'Meta': {'ordering': "['name']", 'object_name': 'Dish'},
            'comments': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'components': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['product.Product']", 'through': u"orm['dish.Component']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128', 'db_index': 'True'}),
            'portions': ('django.db.models.fields.PositiveIntegerField', [], {'default': '2'}),
            'technics': ('django.db.models.fields.CharField', [], {'default': "'redmond'", 'max_length': '20'}),
            'weight': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
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

    complete_apps = ['dish']