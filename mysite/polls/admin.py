# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
# Make the poll app modifiable in the admin
from .models import Question, Choice

#class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
	#Simple arranging information
    #fields = ['pub_date', 'question_text']
    #Adding title (None = No title)
    """
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    """
    # Adding Choice input
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    #Show more information
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    #Add filter panel
    list_filter = ['pub_date']
    #Add search panel
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
