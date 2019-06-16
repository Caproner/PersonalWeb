# -*- coding: utf-8 -*-
from django.db import models


class AgentInfoModel(models.Model):
    name = models.CharField(max_length = 20, verbose_name = u"姓名")
    job = models.CharField(max_length = 20, verbose_name = u"职业")
    rank = models.IntegerField(default = 0, null = False, verbose_name = u"等级")

    class Meta:
        verbose_name = u"干员信息表"
        verbose_name_plural = verbose_name