#!/usr/bin/env python
#coding=utf-8

"""
# base64_test.py
# Created by Leo Wen on Tue Jul 4 16:17:23 CST 2017
"""

import os
import sys
import re
import base64

def test():
    '''Base64 是一种基于 64 个可打印字符来表示二进制数据的表示方法。'''
    encoded = base64.b64encode('data to be encoded')
    print encoded
    data = base64.b64decode(encoded)
    print data

def test1():
    '''Base32 包含 26 个大写字母和 2-7 的数字'''
    encoded = base64.b32encode('data to be encoded')
    print encoded
    data = base64.b32decode(encoded)
    print data

def test2():
    '''Base16 包含 16 个 16 进制大写数字'''
    encoded = base64.b16encode('data to be encoded')
    print encoded
    data = base64.b16decode(encoded)
    print data


if  __name__ == "__main__" :
    test()
    test1()
    test2()
