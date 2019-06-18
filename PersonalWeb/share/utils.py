# -*- coding: utf-8 -*- #
import re
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
import config
import base64
import hashlib 


def safe_int(src):
    """
    转成int
    """
    if not src:
        return src
    else:
        return int(src)

def regex_func(str_param, str_regex):
    p = re.compile(str_regex)
    return p.match(str_param)

def RSA_decode(str_param):
    rsakey = RSA.importKey(config.RSA_PRIVATE_KEY)  # 导入读取到的私钥
    cipher = Cipher_pkcs1_v1_5.new(rsakey)  # 生成对象
    ret = cipher.decrypt(base64.b64decode(str_param), "ERROR")  # 将密文解密成明文，返回的是一个bytes类型数据，需要自己转换成str
    return ret.decode('utf-8')

def hash_code(s, salt='caproner'):# 加点盐
    h = hashlib.sha256()
    s += salt
    h.update(s.encode()) # update方法只接收bytes类型
    return h.hexdigest()

def get_ip(request):
    if 'HTTP_X_FORWARDED_FOR' in request.META:  
        return request.META['HTTP_X_FORWARDED_FOR']  
    else:  
        return request.META['REMOTE_ADDR']