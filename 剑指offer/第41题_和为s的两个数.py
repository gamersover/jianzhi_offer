# -*- coding:utf-8 -*-
"""
剑指offer第41题
问题：输入一个递增排序的数组和一个数字s,在数组中查找两个数使得它们的和正好是s。如果
有多对数字的和为s,输出任意一对即可
思路：一个头指针，一个尾指针，头尾相加如果大于s，尾指针往左，如果小于s，头指针往右，
"""

def find_two_sum(arr, s):
    start = 0
    end = len(arr) - 1
    while(start < end):
        if arr[start] + arr[end] > s:
            end -= 1
        elif arr[start] + arr[end] < s:
            start += 1
        else:
            print(arr[start], arr[end])
            break

arr = [1,2,4,7,11,15]
find_two_sum(arr, 15)