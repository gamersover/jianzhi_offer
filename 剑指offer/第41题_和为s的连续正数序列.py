# -*- coding:utf-8 -*-
"""
剑指offer第41题
问题：输入一个正数s，打印出所有和为s的连续正数序列（至少含有两个数）
思路：
"""

def find_continue_sequence(arr, s):
    if s < 2:
        return
    p1 = 0
    p2 = 1
    p1_move = 0
    p2_move = 0
    curr_sum = arr[p1] + arr[p2]
    while p2 < len(arr):
        curr_sum += p2_move*arr[p2] - p1_move*arr[p1-1]
        if curr_sum == s:
            print(*arr[p1:p2+1], sep=" ")
            p2 += 1
            p1 += 1
            p2_move = 1
            p1_move = 1
        elif curr_sum > s:
            p1 += 1
            p1_move = 1
            p2_move = 0
        else:
            p2 += 1
            p2_move = 1
            p1_move = 0
            
if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8,9]
    s = 17
    find_continue_sequence(arr, s)