# -*- coding:utf-8 -*-
"""
剑指offer第47题
问题：写一个函数，求两个整数之和，要求不能使用加减乘除
思路：用两个数的亦或值表示没有进位的结果sum，用两个数的相与再左移1位表示进位carry,
然后递归的求sum与carry的和即可，知道进位carry为0
"""

def add(num1, num2):
    while 1:
        sum = num1^num2
        carry = (num1&num2)<<1
        num1 = sum
        num2 = carry
        if num2 == 0:
            break
    return num1

print(add(10,0))