# -*- coding: utf-8 -*-
from frontend.model import AgentInfoModel
from share.logs import logger
import random, json


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
    agent_list = AgentInfoModel.filter_rank(agent_rank)
    if len(agent_list) == 0:
        return {}
    rand_agent = random.sample(agent_list.keys(), 1)
    ret = json.loads(agent_list[rand_agent[0]])
    ret['name'] = ret['name'].encode('utf-8').decode('utf-8')
    ret['star'] = get_star(int(ret['rank']))
    logger.debug("Draw %s", ret['name'])
    return ret

def get_ur_pr(agent_save):
    if agent_save < 50:
        return 2
    return (agent_save - 48) * 2

def get_agent_draw(num, agent_save, agent_num):
    agent_list = []
    for i in range(num):
        ur_pr = get_ur_pr(agent_save)
        agent = get_agent(random_rank(ur_pr))
        agent_list.append(agent)
        agent_num[int(agent['rank']) - 3] += 1
        if int(agent['rank']) == 6:
            agent_save = 0
        else:
            agent_save += 1

    agent_draw = {}
    agent_draw['agent_list'] = agent_list
    agent_draw['agent_save'] = agent_save
    for i in range(4):
        agent_draw['agent_' + str(i + 3)] = agent_num[i]

    return agent_draw