#!/usr/bin/env python
#-*- coding: UTF-8 -*-


'''Module: pdb_usage
Created by Leo Wen on 2017-07-06 21:14:48

http://www.cnblogs.com/dkblog/archive/2010/12/07/1980682.html
https://docs.python.org/2/library/bdb.html
'''

import pdb

def test():
    '''Test'''
    print 'Please test here.'
    a = 1
    pdb.set_trace()	#设置断点
    b = 2
    c = a + b
    print (c)

if __name__ == '__main__':
    test()

'''

常用Debug命令：
h(elp)，会打印当前版本Pdb可用的命令，如果要查询某个命令，可以输入 h [command]，例如：“h l” — 查看list命令
l(ist)，可以列出当前将要运行的代码块 
n(ext)，让程序运行下一行，如果当前语句有一个函数调用，用n是不会进入被调用的函数体中的
s(tep)，跟n相似，但是如果当前有一个函数调用，那么s会进入被调用的函数体中
c(ont(inue))，让程序正常运行，直到遇到断点
j(ump)，让程序跳转到指定的行数 
'''
