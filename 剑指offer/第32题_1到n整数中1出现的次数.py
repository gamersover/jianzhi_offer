# -*- coding:utf-8 -*-
"""
剑指offer第32题
问题：输入一个整数n，求出从1到n这n个整数的十进制表示中1出现的次数
思路：先计算个位出现1的次数，在计算十位出现1的次数，依此类推
假设22314，当前位是百位3，前面的数22，后面的数时14
如果当前位大于1，则00 1 **-22 1 **有（前面的数+1）*当前的位数（100）个1
如果当前位等于1，则有前面的数*当前的位数  + 后面的数  + 1个1
如果等于0，则有前面的数*当前的位数个1
"""

def count_one(n):
    i = 1
    count = 0
    while n // i != 0:
        current = (n//i) % 10
        before = n // (i*10)
        after = n - (n//i)*i
        if current > 1:
            count += (before + 1) * i
        elif current == 1:
            count += before * i + after + 1
        elif current == 0:
            count += before * i
        i *= 10
    return count

print(count_one(100))
            