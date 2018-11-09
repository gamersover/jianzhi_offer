# -*- coding:utf-8 -*-
"""
问题：输入一个字符串，打印该字符串中字符的所有排列
思路：不使用递归
"""

def permutation(string):
    if string is None:
        return
    
    count = 0
    print(string)
    count += 1
    if len(string) < 2:
        return
    
    chars = string
    i = 0
    string = string[:i] + string[i+1] + string[i] + string[i+2:]
    i += 1
    while string != chars:
        print(string)
        count += 1
        if i == len(string) - 1:
            string = string[i] + string[1:i] + string[0]
            i = 0
        else: 
            string = string[:i] + string[i+1] + string[i] + string[i+2:]
            i += 1

permutation("abc")
    

