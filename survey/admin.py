__author__ = 'geoffreyboss'

from django.contrib import admin
from survey.models import Survey, Questions, Answers, CompletedSurvey

class QuestionInlineAdmin(admin.StackedInline):
    model = Questions
    extra = 1

class AnswerInlineAdmin(admin.StackedInline):
    model = Answers
    extra = 0

class SurveyAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "posted")
    inlines = [QuestionInlineAdmin]


admin.site.register(Survey, SurveyAdmin)
admin.site.register(Answers)


# Visualize the completed surveys
class CompletedSurveyAdmin(admin.ModelAdmin):
    readonly_fields = ["name", ]
    # display the answers along with the completed survey
    inlines = [AnswerInlineAdmin]

    def save_model(self, request, obj, form, change):
        obj.name = obj.survey.title
        obj.save()


admin.site.register(CompletedSurvey, CompletedSurveyAdmin)
