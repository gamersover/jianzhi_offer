# -*- coding:utf-8 -*-
"""
剑指offer第14题
问题：输入一个整数数组，使得奇数位于偶数前面,报不报证原来的顺序？如果保证顺序，使用思路1，如果不需要保证，使用思路2
思路1：保证顺序，用两个指针，一个指向偶数，一个指向奇数，再拼接一下就可以了
4,1,6,2,3
p1->4->6->2
p2->1->3
返回[p2, p1]就可以
思路2：不保证顺序，用两个指针，一个往后找直到找到偶数，一个往前找直到找到奇数
"""

def order_by_odd(arr):
    arr_odd = []
    arr_even = []
    for item in arr:
        if item % 2 == 0:
            arr_even.append(item)
        else:
            arr_odd.append(item)
    return arr_odd + arr_even

def order_by_odd2(arr):
    start = 0
    end = len(arr) - 1
    while start < end:
        while start<end and arr[start]%2 != 0:
            start += 1
        while start < end and arr[end]%2 == 0:
            end -= 1
        if start<end:
            arr[start], arr[end] = arr[end], arr[start]

arr = [1,2,3,4,5,6]
# print(order_by_odd(arr))

order_by_odd2(arr)
print(arr)
    
