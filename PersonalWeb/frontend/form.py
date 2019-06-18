# -*- coding: utf-8 -*-
from django import forms 
from captcha.fields import CaptchaField
import config
from share.utils import regex_func, RSA_decode


USERNAME_REGEX = r'^[a-z0-9_]{3,16}$'
PASSWORD_REGEX = r'^[a-z0-9_]{6,18}$'


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
        true_password = RSA_decode(self.cleaned_data['password'])
            return true_password
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
        true_password = RSA_decode(self.cleaned_data['password1'])
        if regex_func(true_password, PASSWORD_REGEX):
            return true_password
        else:
            raise forms.ValidationError('密码非法', code='invalid password1')
    
    def clean_password2(self):
        true_password = RSA_decode(self.cleaned_data['password2'])
        return true_password