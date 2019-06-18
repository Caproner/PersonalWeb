# -*- coding: utf-8 -*-
from django.db import models
from share.vals import rds
import json
import config
from share.logs import logger


# 用户信息model
class UserInfoModel(models.Model):
    gender = (
        ('male', '男'),
        ('female', '女'),
    )
    name = models.CharField(max_length = 128, unique = True, verbose_name = u"用户名")
    password = models.CharField(max_length = 256)
    email = models.EmailField(unique = True)
    sex = models.CharField(max_length = 32, choices = gender, default = '女')
    c_time = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['c_time']
        verbose_name = u"用户信息表"
        verbose_name_plural = verbose_name

    def save(self, *args, **kwargs):
        super(UserInfoModel, self).save(*args, **kwargs)
        elem_dict = {
            'name' : self.name,
            'password' : self.password,
            'email' : self.email,
            'sex' : self.sex,
            'c_time' : self.c_time
        }
        try:
            rds.hdel(config.USER_INFO, self.id)
            rds.hset(config.USER_INFO, self.id, json.dumps(elem_dict))
        except Exception as e:
            logger.error('[REDIS]SAVE ERROR %s', e)

    def delete(self, *args, **kwargs):
        try:
            rds.hdel(config.USER_INFO, self.id)
        except Exception as e:
            logger.error('[REDIS]DELETE ERROR %s', e)
        super(UserInfoModel, self).delete(*args, **kwargs)

# 干员信息表model
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
            rds.hdel(config.AGENT_INFO_BY_RANK % self.rank, self.id)
            rds.hset(config.AGENT_INFO_BY_RANK % self.rank, self.id, json.dumps(elem_dict))
        except Exception as e:
            logger.error('[REDIS]SAVE ERROR %s', e)

    def delete(self, *args, **kwargs):
        try:
            rds.hdel(config.AGENT_INFO_BY_RANK % self.rank, self.id)
        except Exception as e:
            logger.error('[REDIS]DELETE ERROR %s', e)
        super(AgentInfoModel, self).delete(*args, **kwargs)

    @classmethod
    def filter_rank(cls, agent_rank):
        agent_list = []

        try:
            agent_list = rds.hgetall(config.AGENT_INFO_BY_RANK % agent_rank)
        except Exception as e:
            logger.error('[REDIS]LGETALL ERROR %s', e)

        if len(agent_list) == 0:
            sql_agent_list = cls.objects.filter(rank = agent_rank)
            if len(sql_agent_list) == 0:
                logger.error("Empty Rank : %s", agent_rank)
                return []
            for var in sql_agent_list:
                agent = {
                    'name' : var.name,
                    'job' : var.job,
                    'rank' : var.rank
                }
                try:
                    rds.hdel(config.AGENT_INFO_BY_RANK % var.rank, var.id)
                    rds.hset(config.AGENT_INFO_BY_RANK % var.rank, var.id, json.dumps(agent))
                except Exception as e:
                    logger.error('[REDIS]SAVE ERROR %s', e)
            try:
                agent_list = rds.hgetall(config.AGENT_INFO_BY_RANK % agent_rank)
            except Exception as e:
                logger.error('[REDIS]LGETALL ERROR %s', e)

        return agent_list