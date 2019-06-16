# -*- coding: utf-8 -*-
from frontend.model import AgentInfoModel
from frontend.share.logs import logger


def get_star(num):
    if not isinstance(num, int):
        return ''
    str = ''
    for i in range(num):
        str += '★'
    return str

def test():
    agent_list = []
    agent_list.append(AgentInfoModel.objects.get(name = u'白面鸮'))
    agent_list.append(AgentInfoModel.objects.get(name = u'史都华德'))
    agent_list.append(AgentInfoModel.objects.get(name = u'星熊'))
    agent_list.append(AgentInfoModel.objects.get(name = u'阿消'))

    ret_list = []
    for var in agent_list:
        ret_list.append({
            'name' : var.name,
            'job' : var.job,
            'rank' : var.rank,
            'star' : get_star(int(var.rank))
        })
        logger.debug("star = %s", get_star(int(var.rank)))

    return ret_list