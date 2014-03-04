# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Survey.body'
        db.delete_column(u'survey_survey', 'body')


    def backwards(self, orm):
        # Adding field 'Survey.body'
        db.add_column(u'survey_survey', 'body',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=355),
                      keep_default=False)


    models = {
        u'survey.answers': {
            'Meta': {'object_name': 'Answers'},
            'answer': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'completed_survey': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['survey.CompletedSurvey']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['survey.Questions']"})
        },
        u'survey.completedsurvey': {
            'Meta': {'object_name': 'CompletedSurvey'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'survey': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['survey.Survey']"})
        },
        u'survey.questions': {
            'Meta': {'object_name': 'Questions'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'survey': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['survey.Survey']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'survey.survey': {
            'Meta': {'object_name': 'Survey'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'posted': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['survey']