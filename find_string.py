#!/usr/bin/env python
#-*- coding: UTF-8 -*-

# 1. 请用 python 编写函数 find_string，从文本中搜索并打印内容，要求支持通配符星号和问号。
# 例子： 
# >>> find_string('hello\nworld\n', 'wor')
# ['wor']
# >>> find_string('hello\nworld\n', 'l*d')
# ['ld']
# >>> find_string('hello\nworld\n', 'o?')
# ['or’]
# 请在下面直接输入，内容会被自动保存。

import re

def find_string(text, keyword):
    '''
    Test example:
    find_string('hello\nworld\n', 'wor')
    ['wor']
    >>> find_string('hello\nworld\n', 'l*d')
    ['ld']
    >>> find_string('hello\nworld\n', 'o?')
    ['or’]
    '''
    if '?' in keyword:
        keyword = re.sub(r'\?', ".", keyword)
    find_result = re.search(keyword, text)
    return [find_result.group()]

import unittest

class FindStringTestCase(unittest.TestCase):
    '''
	unittest.main函数负责实际运行测试，它会实例化所有TestCase的子类，运行所有名字以test开头的方法
	'''
    def test_normal(self):
        result = find_string('hello\nworld\n', 'wor')
        self.failUnless(result == ['wor'], 'Normal find string fail')

    def test_asterisk(self):
        result = find_string('hello\nworld\n', 'l*d')
        self.failUnless(result == ['ld'], 'Asterisk find string fail')

    def test_question_mark(self):
        result = find_string('hello\nworld\n', 'o?')
        self.failUnless(result == ['or'], 'Question mark find string fail')


if __name__ == '__main__':
    unittest.main()

'''
def test():
    print find_string('hello\nworld\n', 'wor')
    print find_string('hello\nworld\n', 'l*d')
    print find_string('hello\nworld\n', 'o?')  


if __name__ == '__main__':
    test()
'''

