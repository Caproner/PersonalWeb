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
        if request.method == 'GET':
            times = int(request.GET.get('times', default='0'))
        if times >= 10:
            times = 10
        elif not times == 0:
            times = 1
        agent_list = get_agent_list(times)
        return render(request, "ArkNights/draw.html", {'agent_list': agent_list})