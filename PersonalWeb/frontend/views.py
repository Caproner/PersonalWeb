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

        if times == 0:
            return render(request, "ArkNights/draw.html")
        
        if times >= 10:
            times = 10
        else:
            times = 1
        agent_list = get_agent_list(times)
        return render(request, "ArkNights/draw_show.html", {'agent_list': agent_list})