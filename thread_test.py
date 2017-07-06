#!/usr/bin/env python
#coding=utf-8

"""
# threadTest.py
# Created by Leo Wen on Thu May 25 18:01:49 CST 2017
"""

import os
import sys
import re

import threading
import time

counter = 0
#mutex = threading.Lock()  #互斥锁
mutex = threading.RLock()  #可重入锁,直到一个线程所有的acquire都被release，其他的线程才能获得资源

#基于threading,Thread的类
class MyThread(threading.Thread):
    
    def __init__(self):
        threading.Thread.__init__(self)
    
    def run(self):
        #声明是全局变量
        global counter,mutex
        time.sleep(1);
        #保证一次只有一个线程使用，保证共享数据操作的完整性
        if mutex.acquire():
            counter += 1
            print "I am %s, set counter:%s" % (self.name, counter)
            mutex.acquire()
            mutex.release()
            mutex.release()

def test1():
    for i in range(0, 200):
        my_thread = MyThread()
        my_thread.start()

'''
    死锁是一个资源被多次调用，而多次调用方都未能释放该资源就会造成死锁，这里结合例子说明下两种常见的死锁情况。
'''
#迭代死锁,该情况是一个线程“迭代”请求同一个资源，直接就会造成死锁：如反复mutex.acquire()，mutex.release()
#就是对同一个锁反复请求，必须


#互相调用死锁
class MyThread1(threading.Thread):
    #线程调用的方法
    def do1(self):
        global resA, resB
        if mutexA.acquire():
            msg = self.name+' got resA'
            print msg
            if mutexB.acquire(1):
                msg = self.name+' got resB'
                print msg
                mutexB.release()
                mutexA.release()
    def do2(self):
        global resA, resB
        if mutexB.acquire():
            msg = self.name+' got resB'
            print msg
            if mutexA.acquire(1):
                msg = self.name+' got resA'
                print msg
                mutexA.release()
                mutexB.release()
    #线程的开始
    def run(self):
        self.do1()
        self.do2()
resA = 0
resB = 0
#mutexA = threading.Lock()
#mutexB = threading.Lock()
#使用可重入锁，
mutexA = threading.RLock()
mutexB = threading.RLock()
def test2():
    for i in range(5):
        t = MyThread1()
        t.start()


#-----------------------------------------
class mythread2(threading.Thread):    # 通过继承创建类
    def __init__(self,threadname):   # 初始化方法
    # 调用父类的初始化方法
        threading.Thread.__init__(self,name = threadname)

    def run(self):             # 重载run方法
        global x,lock       # 使用global表明x为全局变量
        lock.acquire()
        for i in range(3):
            x = x + 1
        time.sleep(1)     # 调用sleep函数，让线程休眠5秒
        print x
        lock.release()
lock = threading.Lock()
def test3():
    tl = []               # 定义列表
    for i in range(10):
        t = mythread2(str(i))        # 类实例化
        tl.append(t)           # 将类对象添加到列表中
    global x
    x=0                 # 将x赋值为0
    for i in tl:
        i.start()


if __name__ == "__main__":
    test3()


















