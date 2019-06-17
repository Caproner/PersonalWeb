# -*- coding: utf-8 -*-
from django.db import models
import frontend.share.vals
import json
import config
from frontend.share.logs import logger


class AgentInfoModel(models.Model):
    name = models.CharField(max_length = 20, verbose_name = u"姓名")
    job = models.CharField(max_length = 20, verbose_name = u"职业")
    rank = models.IntegerField(default = 0, null = False, verbose_name = u"等级")

    class Meta:
        verbose_name = u"干员信息表"
        verbose_name_plural = verbose_name

    def save(self, *args, **kwargs):
        super(AgentInfoModel, self).save(*args, **kwargs)
        elem_dict = {
            'name' : self.name,
            'job' : self.job,
            'rank' : self.rank
        }
        try:
            rds.lpush(config.AGENT_INFO_BY_RANK % self.rank, json.dumps(elem_dict))
        except Exception as e:
            logger.error('ERROR[INFO] %s', e)