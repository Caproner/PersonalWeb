# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import hello_world, HelloWorldView


urlpatterns = [
    url(r'^$', HelloWorldView.as_view(), name="hello_world")
]