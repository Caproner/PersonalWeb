# -*- coding: utf-8 -*-
from django.contrib import admin
from .model import AgentInfoModel, UserInfoModel


@admin.register(UserInfoModel)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'password', 'email', 'sex', 'c_time']
    list_per_page = 25
    ordering = ['id', 'name', 'password', 'email', 'sex', 'c_time']

@admin.register(AgentInfoModel)
class AgentInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'job', 'rank']
    list_per_page = 25
    ordering = ['id', 'name', 'job', 'rank']