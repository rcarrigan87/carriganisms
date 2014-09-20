# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'blogengine_category', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32, primary_key=True)),
            ('cat_slug', self.gf('django.db.models.fields.SlugField')(max_length=128)),
        ))
        db.send_create_signal(u'blogengine', ['Category'])

        # Adding model 'Post'
        db.create_table(u'blogengine_post', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=128)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=180)),
            ('content', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('focus_keyword', self.gf('django.db.models.fields.CharField')(max_length=180, blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('pub_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('main_image', self.gf('django.db.models.fields.URLField')(max_length=128, blank=True)),
            ('main_image_alt', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('og_image', self.gf('django.db.models.fields.URLField')(max_length=128, blank=True)),
            ('og_image_alt', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('views', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'blogengine', ['Post'])

        # Adding M2M table for field category on 'Post'
        m2m_table_name = db.shorten_name(u'blogengine_post_category')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('post', models.ForeignKey(orm[u'blogengine.post'], null=False)),
            ('category', models.ForeignKey(orm[u'blogengine.category'], null=False))
        ))
        db.create_unique(m2m_table_name, ['post_id', 'category_id'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table(u'blogengine_category')

        # Deleting model 'Post'
        db.delete_table(u'blogengine_post')

        # Removing M2M table for field category on 'Post'
        db.delete_table(db.shorten_name(u'blogengine_post_category'))


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'blogengine.category': {
            'Meta': {'object_name': 'Category'},
            'cat_slug': ('django.db.models.fields.SlugField', [], {'max_length': '128'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32', 'primary_key': 'True'})
        },
        u'blogengine.post': {
            'Meta': {'object_name': 'Post'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['blogengine.Category']", 'symmetrical': 'False', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '180'}),
            'focus_keyword': ('django.db.models.fields.CharField', [], {'max_length': '180', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'main_image': ('django.db.models.fields.URLField', [], {'max_length': '128', 'blank': 'True'}),
            'main_image_alt': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'og_image': ('django.db.models.fields.URLField', [], {'max_length': '128', 'blank': 'True'}),
            'og_image_alt': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'pub_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '128'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'views': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['blogengine']