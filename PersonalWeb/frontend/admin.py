# -*- coding: utf-8 -*-
from django.contrib import admin
from .model import AgentInfoModel


@admin.register(AgentInfoModel)
class AgentInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'job', 'rank']
    list_per_page = 25
    ordering = ['id', 'name', 'job', 'rank']