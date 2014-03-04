# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Answers'
        db.create_table(u'survey_answers', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('answer', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['survey.Questions'])),
            ('completed_survey', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['survey.CompletedSurvey'])),
        ))
        db.send_create_signal(u'survey', ['Answers'])

        # Adding model 'CompletedSurvey'
        db.create_table(u'survey_completedsurvey', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('survey', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['survey.Survey'])),
        ))
        db.send_create_signal(u'survey', ['CompletedSurvey'])


    def backwards(self, orm):
        # Deleting model 'Answers'
        db.delete_table(u'survey_answers')

        # Deleting model 'CompletedSurvey'
        db.delete_table(u'survey_completedsurvey')


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
            'body': ('django.db.models.fields.CharField', [], {'max_length': '355'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'posted': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['survey']