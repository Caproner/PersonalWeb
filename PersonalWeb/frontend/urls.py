# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import hello_world, HelloWorldView


urlpatterns = [
    url(r'/(?P<id>\d+)/(?P<docs>[a-zA-Z\u4E00-\u9FA5]*)$', HelloWorldView.as_view(), name="hello_world")
]