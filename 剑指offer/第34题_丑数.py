# -*- coding:utf-8 -*-
"""
剑指offer第34题
问题：只包含因子2,3,5的称为丑数，求按小到大的顺序的第1500个丑数，习惯上把1当做第一个丑数
思路：
假设数组中已经有若干个排好序的丑数，并且其中最大的丑数为M。那么下一个丑数一定是数组中某个数乘以2或3或5的结果，
所以我们把数组中的每个数都乘以2，找到第一个大于M的结果M2（小于等于M的结果肯定已经在数组中了，不需要考虑）；
同理，把数组中的每个数都乘以3，找到第一个大于M的结果M3；把数组中的每个数都乘以5，找到第一个大于M的结果M5。
那么下一个丑数一定是M2、M3、M5当中的最小值。
实际上，在寻找M2、M3、M5的过程中，不需要每次都从头开始遍历，只要记住上一次遍历到的位置，继续往后遍历即可。
"""


def get_ugly_number(n):
    a = [1]
    t1 = 0
    t2 = 0
    t3 = 0
    for i in range(1,n):
        min_number = min(a[t1]*2, a[t2]*3, a[t3]*5)
        a.append(min_number)
        while a[t1] * 2 <= min_number:
            t1 += 1
        while a[t2] * 3 <= min_number:
            t2 += 1
        while a[t3] * 5 <= min_number:
            t3 += 1
    return a[n-1]

print(get_ugly_number(1500))