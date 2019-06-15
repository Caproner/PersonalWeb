# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.generic.base import View
from django.shortcuts import render


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "index.html")

class ArkDrawView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "ArkNights/draw.html")