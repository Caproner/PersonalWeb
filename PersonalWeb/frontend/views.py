# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.generic.base import View
from django.shortcuts import render, redirect
from frontend.ArkNights.draw import get_agent_draw
from share.logs import logger
from frontend.model import UserInfoModel
from frontend.form import UserForm, RegisterForm


class NotFoundView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "404.html")

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "index.html")

class LoginView(View):
    def get(self, request, *args, **kwargs):
        if request.session.get('is_login',None):
            return redirect('/index')
        login_form = UserForm()
        return render(request, "login.html", {'login_form':login_form})
    def post(self, request, *args, **kwargs):
        if request.session.get('is_login',None):
            return redirect('/index')
        if request.method == 'POST':
            login_form = UserForm(request.POST)
            message = "请检查填写的内容！"
            if login_form.is_valid():
                username = login_form.cleaned_data['username']
                password = login_form.cleaned_data['password'] 
                username = username.strip()
                try:
                    user = UserInfoModel.get_user(username) 
                    if user['password'] == password: 
                        request.session['is_login'] = True
                        request.session['user_name'] = user['name']
                        return redirect('/index') 
                    else:
                        message = "密码不正确！"
                except:
                    message = "用户名不存在！"
            return render(request, 'login.html', {'message':message, 'login_form':login_form})

        login_form = UserForm()
        return render(request, 'login.html', {'message':message, 'login_form':login_form})

class RegisterView(View):
    def get(self, request, *args, **kwargs):
        if request.session.get('is_login', None): # 登录状态不允许注册。你可以修改这条原则！
            return redirect("/index")
        register_form = RegisterForm()
        return render(request, "register.html", {'register_form':register_form})
    def post(self, request, *args, **kwargs):
        if request.session.get('is_login',None):
            return redirect('/index')
        if request.method == 'POST':
            register_form = RegisterForm(request.POST)
            message = "请检查填写的内容！"
            if register_form.is_valid():
                username = register_form.cleaned_data['username']
                password1 = register_form.cleaned_data['password1'] 
                password2 = register_form.cleaned_data['password2'] 
                email = register_form.cleaned_data['email']
                sex = register_form.cleaned_data['sex']
                username = username.strip()
                if UserInfoModel.get_user(username) != {}:
                    message = '用户名已被占用'
                elif UserInfoModel.get_username_from_email(email) != '':
                    message = '邮箱已被占用'
                else:
                    new_user = UserInfoModel()
                    new_user.name = username
                    new_user.password = password1
                    new_user.email = email
                    new_user.sex = sex
                    new_user.save()
                    return redirect('/index')
            return render(request, 'register.html', {'message':message, 'register_form':register_form})

        register_form = UserForm()
        return render(request, 'register.html', {'message':message, 'register_form':register_form})

class LogoutView(View):
    def get(self, request, *args, **kwargs):
        if not request.session.get('is_login', None): # 如果本来就未登录，也就没有登出一说
            return redirect("/index")
        request.session.flush()
        return redirect("/index")

class ArkDrawView(View):
    def get(self, request, *args, **kwargs):
        if request.method == 'GET':
            times = int(request.GET.get('times', default='0'))
            agent_times = int(request.GET.get('agent_times', default='0'))
            agent_save = int(request.GET.get('agent_save', default='0'))
            agent_num = [0, 0, 0, 0]
            agent_num[0] = int(request.GET.get('agent_3', default='0'))
            agent_num[1] = int(request.GET.get('agent_4', default='0'))
            agent_num[2] = int(request.GET.get('agent_5', default='0'))
            agent_num[3] = int(request.GET.get('agent_6', default='0'))

        if times == 0:
            return render(request, "ArkNights/draw.html")

        if times >= 10:
            times = 10
        else:
            times = 1
        agent_draw = get_agent_draw(times, agent_save, agent_num)

        return render(request, "ArkNights/draw_main.html", {
            'agent_list' : agent_draw['agent_list'],
            'agent_times' : agent_times + times,
            'agent_save' : agent_draw['agent_save'],
            'agent_3' : agent_draw['agent_3'],
            'agent_4' : agent_draw['agent_4'],
            'agent_5' : agent_draw['agent_5'],
            'agent_6' : agent_draw['agent_6']
            })