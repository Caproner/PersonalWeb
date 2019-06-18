# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.generic.base import View
from django.shortcuts import render, redirect
from frontend.ArkNights.draw import get_agent_draw
from share.logs import logger
from frontend.model import UserInfoModel
from frontend.form import UserForm, RegisterForm
from share.utils import hash_code, get_ip


class NotFoundView(View):
    def get(self, request, *args, **kwargs):
        ip = get_ip(request)
        logger.debug("[%s]: 404", ip)
        return render(request, "404.html")

class IndexView(View):
    def get(self, request, *args, **kwargs):
        ip = get_ip(request)
        logger.debug("[%s](%s): Open /index", ip, request.session.get('user_name', None))
        return render(request, "index.html")

class LoginView(View):
    def get(self, request, *args, **kwargs):
        ip = get_ip(request)
        if request.session.get('is_login', None):
            logger.debug("[%s](%s): [IRR]Try to login again, but aborted", ip, request.session.get('user_name', None))
            return redirect('/index')
        login_form = UserForm()
        logger.debug("[%s]: Open /login", ip)
        return render(request, "login.html", {'login_form':login_form})
    def post(self, request, *args, **kwargs):
        ip = get_ip(request)
        if request.session.get('is_login', None):
            logger.debug("[%s](%s): [IRR]Try to post login form, but aborted", ip, request.session.get('user_name', None))
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
                    if user['password'] == hash_code(password): 
                        request.session['is_login'] = True
                        request.session['user_name'] = user['name']
                        logger.debug("[%s](%s): Login Success", ip, request.session.get('user_name', None))
                        return redirect('/index') 
                    else:
                        message = "密码不正确！"
                except:
                    message = "用户名不存在！"
            logger.debug("[%s]: Login Failed", ip)
            return render(request, 'login.html', {'message':message, 'login_form':login_form})
        logger.debug("[%s](%s): [IRR]post login query but not a form", ip, request.session.get('user_name', None))
        login_form = UserForm()
        return render(request, 'login.html', {'message':message, 'login_form':login_form})

class RegisterView(View):
    def get(self, request, *args, **kwargs):
        ip = get_ip(request)
        if request.session.get('is_login', None): # 登录状态不允许注册。你可以修改这条原则！
            logger.debug("[%s](%s): Try to register again, but aborted", ip, request.session.get('user_name', None))
            return redirect("/index")
        register_form = RegisterForm()
        logger.debug("[%s]: Open /register", ip)
        return render(request, "register.html", {'register_form':register_form})
    def post(self, request, *args, **kwargs):
        ip = get_ip(request)
        if request.session.get('is_login',None):
            logger.debug("[%s](%s): [IRR]Try to post register form, but aborted", ip, request.session.get('user_name', None))
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
                    message = '用户名非法：用户名已被占用'
                elif UserInfoModel.get_username_from_email(email) != '':
                    message = '邮箱非法：邮箱已被占用'
                elif password1 != password2:
                    message = '密码非法：两次输入密码不一致'
                else:
                    new_user = UserInfoModel()
                    new_user.name = username
                    new_user.password = hash_code(password1)
                    new_user.email = email
                    new_user.sex = sex
                    new_user.save()
                    logger.debug("[%s]: Register Success", ip)
                    return redirect('/index')
            logger.debug("[%s]: Register Failed", ip)
            return render(request, 'register.html', {'message':message, 'register_form':register_form})

        register_form = UserForm()
        logger.debug("[%s](%s): [IRR]post register query but not a form", ip, request.session.get('user_name', None))
        return render(request, 'register.html', {'message':message, 'register_form':register_form})

class LogoutView(View):
    def get(self, request, *args, **kwargs):
        ip = get_ip(request)
        if not request.session.get('is_login', None): # 如果本来就未登录，也就没有登出一说
            logger.debug("[%s]: [IRR]Try to logout without login, but aborted", ip)
            return redirect("/index")
        logger.debug("[%s](%s): Logout Success", ip, request.session.get('user_name', None))
        request.session.flush()
        return redirect("/index")

class ArkDrawView(View):
    def get(self, request, *args, **kwargs):
        ip = get_ip(request)
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
            logger.debug("[%s](%s): Open /ArkNights/draw", ip, request.session.get('user_name', None))
            return render(request, "ArkNights/draw.html")

        if times >= 10:
            times = 10
        else:
            times = 1
        agent_draw = get_agent_draw(times, agent_save, agent_num)

        logger.debug("[%s](%s): \nDraw result: %s\nUrl: %s", ip, request.session.get('user_name', None), agent_draw['agent_list'], request.get_full_path())

        return render(request, "ArkNights/draw_main.html", {
            'agent_list' : agent_draw['agent_list'],
            'agent_times' : agent_times + times,
            'agent_save' : agent_draw['agent_save'],
            'agent_3' : agent_draw['agent_3'],
            'agent_4' : agent_draw['agent_4'],
            'agent_5' : agent_draw['agent_5'],
            'agent_6' : agent_draw['agent_6']
            })