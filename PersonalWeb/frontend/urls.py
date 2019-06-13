# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import hello_world


urlpatterns = [
    url(r'^$', url(hello_world), name="hello_world")
]