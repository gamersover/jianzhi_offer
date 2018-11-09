# -*- coding:utf-8 -*-
"""
剑指offer第45题
问题：0,1,...,n-1这n个数排成一个圆圈，从数字0开始每次从这个圆圈中删除第m个数字，
然后从下一个数字开始，删除第m个数，求出这个圆圈里剩下的最后一个数字。
思路：约瑟夫环问题
"""

def last_remaining(n, m):
    last = 0
    for i in range(2,n+1):
        last = (last+m) % i
        print(last)
    return last

print(last_remaining(5, 5))


