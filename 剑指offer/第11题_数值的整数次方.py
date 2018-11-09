# -*- coding:utf-8 -*-
"""
剑指offer第11题
问题：求一个数的整数次方
思路：直接连乘，注意负指数，按理需考虑0的负数次幂没意义，还有一种思路递归
通过测试，递归慢了很多
"""
import time

def power(x, n):
    if n < 0:
        return 1/power_with_expoment(x, -n)
    else:
        return power_with_expoment(x, n)

def power_with_expoment(x, n):
    res = 1
    for i in range(n):
        res *= x
    return res

def power_with_recursive(x, n):
    if n == 1:
        return x
    elif n % 2 == 0:
        return power_with_recursive(x, n//2) * power_with_recursive(x, n//2)
    else:
        return power_with_recursive(x, (n-1)//2) * power_with_recursive(x, (n-1)//2) * x

curr_time = time.time()
print(power(3.1, 3))
next_time = time.time()
print(power_with_recursive(3.1, 3))
final_time = time.time()
print(next_time-curr_time)
print(final_time-next_time)
