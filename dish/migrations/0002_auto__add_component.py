# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Component'
        db.create_table(u'dish_component', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dish', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dish.Dish'])),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['product.Product'])),
            ('weight', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
        ))
        db.send_create_signal(u'dish', ['Component'])


    def backwards(self, orm):
        # Deleting model 'Component'
        db.delete_table(u'dish_component')


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
            'components': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['product.Product']", 'through': u"orm['dish.Component']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'portions': ('django.db.models.fields.PositiveIntegerField', [], {'default': '2'})
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