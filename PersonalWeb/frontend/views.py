# -*- coding: utf-8 -*-
from django.http import HttpResponse


def hello_world(request):
    return HttpResponse('hello world')