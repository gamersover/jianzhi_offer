# -*- coding:utf-8 -*-
"""
剑指offer第9题
问题：求斐波那契数列的前n项
"""


def fibonacci(n):
    a = 0
    b = 1
    print(a, end=" ")
    for i in range(1,n):
        a,b = b,a+b
        print(a, end=" ")

fibonacci(6)
    
    