#!/usr/bin/env python
#coding=utf-8

"""
# timeit_test.py
# Created by Leo Wen on 2017年 7月 4日 星期二 18时30分00秒 CST
"""

import os
import sys
import re

import timeit
'''
This module provides a simple way to time small bits of Python code.
It has both a Command-Line Interface as well as a callable one. 
It avoids a number of common traps for measuring execution times. 
See also Tim Peters’ introduction to the “Algorithms” chapter in the Python Cookbook, published by O’Reilly.
https://docs.python.org/2/library/timeit.html
'''

def test1():	
	print "test1:", timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
	
def test2():
	#default number = 1000000
	t1 = timeit.Timer("x = range(100)")
	print "test2:", t1.timeit()
	print "test2:", t1.timeit(number = 10000)
	
	#default repeat = 3, will return a list.
	print "test2:", t1.repeat(repeat = 5, number = 10000)
	
def print_hello():
	for i in range(10):
		x = i
		
def test3():
	#timeit.timeit(stmt='pass', setup='pass', timer=<default timer>, number=1000000)
	#
	print "test3:",timeit.timeit("print_hello()", setup="from __main__ import print_hello")
	print "test3:",timeit.timeit("print_hello()", setup="from __main__ import print_hello", number=1000)
		

if  __name__ == "__main__" :
	#test1()
	#test2()
	test3()