# -*- coding: utf-8 -*-
from redis import StrictRedis
import config

rds = StrictRedis(host = config.REDIS_HOST, port = config.REDIS_PORT, db = config.REDIS_DB)