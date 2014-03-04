from django.db import models

# Create your models here.

class Survey(models.Model):
    title = models.CharField(max_length=100)
    posted = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title

class Questions(models.Model):
    question = models.CharField(max_length=255)
    survey = models.ForeignKey(Survey)

    def __unicode__(self):
        return self.question

class CompletedSurvey(models.Model):
    name = models.CharField(max_length=250)
    survey = models.ForeignKey(Survey)

    def __unicode__(self):
        return self.name

class Answers(models.Model):
    answer = models.CharField(max_length=100)
    question = models.ForeignKey(Questions)
    completed_survey = models.ForeignKey(CompletedSurvey)

    def __unicode__(self):
        return self.answer
