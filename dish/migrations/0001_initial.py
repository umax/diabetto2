# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Dish'
        db.create_table(u'dish_dish', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
            ('portions', self.gf('django.db.models.fields.PositiveIntegerField')(default=2)),
        ))
        db.send_create_signal(u'dish', ['Dish'])


    def backwards(self, orm):
        # Deleting model 'Dish'
        db.delete_table(u'dish_dish')


    models = {
        u'dish.dish': {
            'Meta': {'ordering': "['name']", 'object_name': 'Dish'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'portions': ('django.db.models.fields.PositiveIntegerField', [], {'default': '2'})
        }
    }

    complete_apps = ['dish']