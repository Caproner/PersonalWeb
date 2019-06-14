# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.generic.base import View
from django.shortcuts import render
from .share.utils import safe_int


class HelloWorldView(View):
    def get(self, request, *args, **kwargs):
        docs = kwargs.get('docs')
        article_id = safe_int(kwargs.get('id'))
        return render(request, "hello_world.html", dict(id=article_id, name=docs))

def hello_world(request):
    return HttpResponse('hello world')