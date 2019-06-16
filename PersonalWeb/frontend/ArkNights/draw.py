# -*- coding: utf-8 -*-
from frontend.model import AgentInfoModel

def get_star(num):
    if not isinstance(num, int):
        return ''
    str = ''
    for i in range(num):
        str += '★'
    return str

def test():
    agent_list = []
    agent_list.append(AgentInfoModel.objects.get(name = '白面鸮'))
    agent_list.append(AgentInfoModel.objects.get(name = '史都华德'))
    agent_list.append(AgentInfoModel.objects.get(name = '星熊'))
    agent_list.append(AgentInfoModel.objects.get(name = '阿消'))

    for var in agent_list:
        var['star'] = get_star(var['rank'])
    return agent_list