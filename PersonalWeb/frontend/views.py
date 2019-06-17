# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.generic.base import View
from django.shortcuts import render
from frontend.ArkNights.draw import get_agent_draw
from share.logs import logger


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "index.html")

class ArkDrawView(View):
    def get(self, request, *args, **kwargs):
        if request.method == 'GET':
            times = int(request.GET.get('times', default='0'))
            agent_times = int(request.GET.get('agent_times', default='0'))
            agent_save = int(request.GET.get('agent_save', default='0'))
            agent_num = [0, 0, 0, 0]
            agent_num[0] = int(request.GET.get('agent_3', default='0'))
            agent_num[1] = int(request.GET.get('agent_4', default='0'))
            agent_num[2] = int(request.GET.get('agent_5', default='0'))
            agent_num[3] = int(request.GET.get('agent_6', default='0'))

        if times == 0:
            return render(request, "ArkNights/draw.html")

        if times >= 10:
            times = 10
        else:
            times = 1
        agent_draw = get_agent_draw(times, agent_save, agent_num)

        return render(request, "ArkNights/draw_main.html", {
            'agent_list' : agent_draw['agent_list'],
            'agent_times' : agent_times + times,
            'agent_save' : agent_draw['agent_save'],
            'agent_3' : agent_draw['agent_3'],
            'agent_4' : agent_draw['agent_4'],
            'agent_5' : agent_draw['agent_5'],
            'agent_6' : agent_draw['agent_6']
            })