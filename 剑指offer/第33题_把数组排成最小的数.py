# -*- coding:utf-8 -*-
"""
剑指offer第33题
问题：输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接的所有数字的最小的一个
思路：定义如下法则比较两个字符串的大小
如果ab > ba则a>b 表示a与b拼接时，b在前面拼接后的值会小，b小于a
如果ab < ba,则a < b，表明a放在前面比较好
如果ab = ba，则a==b
按照以上比较法则对数组进行排序，最小的值必须放在最前面，从而排序后的次序刚好就是最小值
"""

def print_min(arr):
    str_arr = list(map(str, arr))
    print(*sort_arr(str_arr), sep='')

def sort_arr(str_arr):
    if len(str_arr) < 1:
        return []
    main_number = str_arr[0]
    left = [i for i in str_arr if is_small(i, main_number)==1]
    mid = [i for i in str_arr if is_small(i, main_number)==0]
    right = [i for i in str_arr if is_small(i, main_number)==-1]
    return sort_arr(left) + mid + sort_arr(right)

def is_small(a, b):
    if a + b > b + a:
        return -1
    elif a + b < b + a:
        return 1
    else:
        return 0 
    
print_min([3,32,321])