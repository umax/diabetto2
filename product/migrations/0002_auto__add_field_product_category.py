# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Product.category'
        db.add_column(u'product_product', 'category',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['category.Category'], null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Product.category'
        db.delete_column(u'product_product', 'category_id')


    models = {
        u'category.category': {
            'Meta': {'ordering': "['name']", 'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'product.product': {
            'Meta': {'ordering': "['name']", 'object_name': 'Product'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['category.Category']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['product']