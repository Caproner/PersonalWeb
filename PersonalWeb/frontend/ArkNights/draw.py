# -*- coding: utf-8 -*-
from frontend.model import AgentInfoModel

def get_star(num):
    if not isinstance(num, int):
        return ''
    str = ''
    for i in range(num):
        str += '★'
    return str