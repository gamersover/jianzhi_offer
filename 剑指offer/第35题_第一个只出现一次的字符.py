# -*- coding:utf-8 -*-
"""
剑指offer第35题
问题：在字符串中找出第一个只出现一次的字符
思路：遍历字符串，将字符串与字符串出现的次数记下来作为（键值对），然后遍历字典中第一个值为1的键就可以了
"""
from collections import OrderedDict

def get_fisrt_char(string):
    order_dict = OrderedDict()
    for ch in string:
        if ch not in order_dict:
            order_dict[ch] = 1
        else:
            order_dict[ch] += 1
    
    for i in order_dict:
        if order_dict[i] == 1:
            return i
    return None

print(get_fisrt_char("abaccdeff"))