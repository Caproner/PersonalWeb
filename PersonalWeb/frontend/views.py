# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.generic.base import View
from django.shortcuts import render


class HelloWorldView(View):
    def get(self, request):
        return render(request, "hello_world.html", dict(value="hello world"))

def hello_world(request):
    return HttpResponse('hello world')