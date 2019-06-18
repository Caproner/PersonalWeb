# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^(|index)$', IndexView.as_view(), name="index"),
    url(r'^ArkNights/draw$', ArkDrawView.as_view(), name="ark_draw"),
    url(r'^login$', LoginView.as_view()),
    url(r'^register$', RegisterView.as_view()),
    url(r'^logout$', LogoutView.as_view()),
    url(r'^404$', NotFoundView.as_view()),
    #url(r'^(?P<id>\d+)/(?P<docs>[a-zA-Z\u4E00-\u9FA5]*)$', HelloWorldView.as_view(), name="hello_world")
]