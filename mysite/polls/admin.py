# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
# Make the poll app modifiable in the admin
from .models import Question

admin.site.register(Question)
