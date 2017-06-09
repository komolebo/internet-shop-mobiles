# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Mobile


# class ChoiceInline(admin.StackedInline):
#     model = Choice
#     extra = 3


# class PollAdmin(admin.ModelAdmin):
#     inlines = [ChoiceInline]
#

# admin.site.register(Poll, PollAdmin)
admin.site.register(Mobile)