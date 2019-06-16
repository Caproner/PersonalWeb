# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.generic.base import View
from django.shortcuts import render
from .model import AgentInfoModel


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "index.html")

class ArkDrawView(View):
    def get(self, request, *args, **kwargs):

        sliver_grey = AgentInfoModel(name = '银灰', job = '近卫', rank = 6)
        sliver_grey.save()

        agent_list = [
            {'name' : '炎熔', 'job' : '术师', 'rank' : 3, 'star' : '★★★'},
            {'name' : '炎熔', 'job' : '术师', 'rank' : 3, 'star' : '★★★'},
            {'name' : '炎熔', 'job' : '术师', 'rank' : 3, 'star' : '★★★'},
            {'name' : '炎熔', 'job' : '术师', 'rank' : 3, 'star' : '★★★'},
            {'name' : '炎熔', 'job' : '术师', 'rank' : 3, 'star' : '★★★'},
            {'name' : '炎熔', 'job' : '术师', 'rank' : 3, 'star' : '★★★'},
            {'name' : '炎熔', 'job' : '术师', 'rank' : 3, 'star' : '★★★'},
            {'name' : '炎熔', 'job' : '术师', 'rank' : 3, 'star' : '★★★'},
            {'name' : '炎熔', 'job' : '术师', 'rank' : 3, 'star' : '★★★'},
            {'name' : '炎熔', 'job' : '术师', 'rank' : 3, 'star' : '★★★'}
        ]
        '''
        agent_list = [
            {'name' : '能天使', 'job' : '狙击', 'rank' : 6, 'star' : '★★★★★★'},
            {'name' : '天火', 'job' : '术师', 'rank' : 5, 'star' : '★★★★★'},
            {'name' : '玫兰莎', 'job' : '近卫', 'rank' : 3, 'star' : '★★★'},
            {'name' : '红豆', 'job' : '先锋', 'rank' : 4, 'star' : '★★★★'}
            ]
        '''
        return render(request, "ArkNights/draw.html", {'agent_list': agent_list})