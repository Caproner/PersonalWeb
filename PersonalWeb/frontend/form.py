# -*- coding: utf-8 -*-
from django import forms 
from captcha.fields import CaptchaField
import re

USERNAME_REGEX = r'^[a-z0-9_]{3,16}$'
PASSWORD_REGEX = r'^[a-z0-9_]{6,18}$'

def regex_func(str, str_regex):
    p = re.compile(str_regex)
    return p.match(str)


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
        if regex_func(self.cleaned_data['username'], USERNAME_REGEX):
            return self.cleaned_data['username']
        else:
            raise forms.ValidationError('用户名非法', code='invalid username')
    
    def clean_password(self):
        if regex_func(self.cleaned_data['password'], PASSWORD_REGEX):
            return self.cleaned_data['password']
        else:
            raise forms.ValidationError('密码非法', code='invalid password')

class RegisterForm(forms.Form):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    username = forms.CharField(
        label="用户名", 
        max_length=128, 
        widget=forms.TextInput(attrs={'class': 'form-control'})
        )
    password1 = forms.CharField(
        label="密码", 
        max_length=256, 
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
        )
    password2 = forms.CharField(
        label="确认密码", 
        max_length=256, 
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
        )
    email = forms.EmailField(
        label="邮箱地址", 
        widget=forms.EmailInput(attrs={'class': 'form-control'})
        )
    sex = forms.ChoiceField(
        label='性别', 
        choices=gender
        )
    captcha = CaptchaField(label='验证码')

    def clean_username(self):
        if regex_func(self.cleaned_data['username'], USERNAME_REGEX):
            return self.cleaned_data['username']
        else:
            raise forms.ValidationError('用户名非法', code='invalid username')
    
    def clean_password1(self):
        if regex_func(self.cleaned_data['password1'], PASSWORD_REGEX):
            return self.cleaned_data['password1']
        else:
            raise forms.ValidationError('密码非法', code='invalid password1')

    def clean_password2(self):
        if self.cleaned_data['password1'] == self.cleaned_data['password2']:
            return self.cleaned_data['password2']
        else:
            raise forms.ValidationError('密码不一致', code='invalid password2')