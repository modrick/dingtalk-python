#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2017/11/28 上午11:47
# @Author : Matrix
# @Github : https://github.com/blackmatrix7/
# @Blog : http://www.cnblogs.com/blackmatrix/
# @File : token.py
# @Software: PyCharm
import hashlib
import requests
from .configs import *
from .foundation import dingtalk_resp

__author__ = 'blackmatrix'


@dingtalk_resp
def get_access_token(corp_id, corp_secret):
    """
    获取Access Token
    :return:
    """
    payload = {'corpid': corp_id, 'corpsecret': corp_secret}
    return requests.get(DING_GET_ACCESS_TOKEN, params=payload)


@dingtalk_resp
def get_jsapi_ticket(accsess_token):
    params = {'access_token': accsess_token}
    data = requests.get(DING_GET_JSAPI_TICKET, params=params)
    return data


def generate_jsapi_signature(**kwargs):
    keys = sorted(kwargs)
    plain = ''
    for key in keys:
        plain += '{0}={1}&'.format(key, kwargs.get(key))
    plain = plain.strip('&')
    plain_bytes = plain.encode('utf-8')
    sha1 = hashlib.sha1(plain_bytes).hexdigest()
    return sha1

if __name__ == '__main__':
    pass
