# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Dish.technics'
        db.add_column(u'dish_dish', 'technics',
                      self.gf('django.db.models.fields.CharField')(default='redmond', max_length=20),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Dish.technics'
        db.delete_column(u'dish_dish', 'technics')


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
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'portions': ('django.db.models.fields.PositiveIntegerField', [], {'default': '2'}),
            'technics': ('django.db.models.fields.CharField', [], {'default': "'redmond'", 'max_length': '20'})
        },
        u'product.product': {
            'Meta': {'ordering': "['name']", 'unique_together': "(('name', 'category'),)", 'object_name': 'Product'},
            'carbohydrates': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['category.Category']", 'null': 'True'}),
            'glycemic_index': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['dish']