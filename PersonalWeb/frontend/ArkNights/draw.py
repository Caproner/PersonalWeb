# -*- coding: utf-8 -*-
from frontend.model import AgentInfoModel
from frontend.share.logs import logger
import random


def get_star(num):
    if not isinstance(num, int):
        return ''
    str = ''
    for i in range(num):
        str += '★'
    return str

def random_rank(ur_pr):
    rand_num = random.randint(0, 99)
    if rand_num < ur_pr:
        return 6
    else:
        rand_num = random.randint(0, 97)
        if rand_num < 40:
            return 3
        elif rand_num < 90:
            return 4
        else:
            return 5

def get_agent(agent_rank):
    agent_list = AgentInfoModel.objects.filter(rank = agent_rank)
    if len(agent_list) == 0:
        logger.error("Empty Rank : %s", agent_rank)
        return {}
    rand_num = random.randint(0, len(agent_list) - 1)
    ret = {
        'name' : agent_list[rand_num].name,
        'job' : agent_list[rand_num].job,
        'rank' : agent_list[rand_num].rank,
        'star' : get_star(int(agent_list[rand_num].rank))
    }
    logger.debug("Draw %s", ret['name'])
    return ret


def get_agent_list(num):
    agent_list = []
    for i in range(num):
        agent_list.append(get_agent(random_rank(2)))
    return agent_list