# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.generic.base import View
from django.shortcuts import render
from frontend.ArkNights.draw import get_agent_list


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "index.html")

class ArkDrawView(View):
    def get(self, request, *args, **kwargs):

        '''
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

        agent_list = [
            {'name' : '能天使', 'job' : '狙击', 'rank' : 6, 'star' : get_star(6)},
            {'name' : '天火', 'job' : '术师', 'rank' : 5, 'star' : get_star(5)},
            {'name' : '玫兰莎', 'job' : '近卫', 'rank' : 3, 'star' : get_star(3)},
            {'name' : '红豆', 'job' : '先锋', 'rank' : 4, 'star' : get_star(4)}
            ]
        '''
        agent_list = get_agent_list(10)
        return render(request, "ArkNights/draw.html", {'agent_list': agent_list})