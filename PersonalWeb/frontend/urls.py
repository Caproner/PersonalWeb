# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import IndexView, ArkDrawView


urlpatterns = [
    url(r'^(|index.html)$', IndexView.as_view(), name="index"),
    url(r'^ArkNights/draw.html$', ArkDrawView.as_view(), name="ark_draw"),
    #url(r'^(?P<id>\d+)/(?P<docs>[a-zA-Z\u4E00-\u9FA5]*)$', HelloWorldView.as_view(), name="hello_world")
]