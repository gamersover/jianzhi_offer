# -*- coding:utf-8 -*-
'''
剑指offer第10题
问题：输入一个整数，输出该数二进制表示中1的个数
思路：整数n与n-1按位相与后可以将n的二进制表示右边的第一个1变为0,其他位上1不变，
利用该关系，循环执行n^n-1,当整数n变为全0(即0)的步数即为1的个数
'''
def get_one_number(n):
    count = 0
    while n:
        count += 1
        n = n & n-1
    return count

res = get_one_number(1024)
print(res)   

