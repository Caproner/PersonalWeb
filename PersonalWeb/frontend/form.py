# -*- coding: utf-8 -*-
from django import forms 
from captcha.fields import CaptchaField
import re


class UserForm(forms.Form):
    username = forms.CharField(
        label="用户名", 
        max_length=128, 
        widget=forms.TextInput(attrs={'class': 'form-control'})
        )
    password = forms.CharField(
        label="密码", 
        max_length=256, 
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
        )
    captcha = CaptchaField(label='验证码')

    def clean_username(self):
        username = self.cleaned_data['username']
        username_regex = r'^[a-z0-9_]{3,16}$'
        p = re.compile(username_regex)
        if p.match(username):
            return username
        else:
            raise forms.ValidationError('用户名非法', code='invalid username')
    
    def clean_password(self):
        password = self.cleaned_data['password']
        password_regex = r'^[a-z0-9_]{6,18}$'
        p = re.compile(password_regex)
        if p.match(password):
            return password
        else:
            raise forms.ValidationError('密码非法', code='invalid password')