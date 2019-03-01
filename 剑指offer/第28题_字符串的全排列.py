# -*- coding:utf-8 -*-
"""
问题：输入一个字符串，打印该字符串中字符的所有排列
思路：交换位置，递归
"""

def permutation(char_arr):
    if len(char_arr) == 1:
        return [char_arr]
    all_res = []
    for i in range(0, len(char_arr)):
        char_arr[0], char_arr[i] = char_arr[i], char_arr[0]
        res = permutation(char_arr[1:])
        for r in res:
            all_res.append(char_arr[0] + ''.join(r))
        char_arr[0], char_arr[i] = char_arr[i], char_arr[0]
    return all_res


s = "5462"
print(permutation(list(s)))
    

