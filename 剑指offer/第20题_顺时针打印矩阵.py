# -*- coding:utf-8 -*-
"""
剑指offer第20题
问题：输入一个矩阵，按照从外向里以顺时针的顺序打印出每一个元素
思路：比如矩阵
 1  2  3  4  5
 7  8  9 10 11
12 13 14 15 16
以圈计算，第一圈1 2 3 4 5 11 16 15 14 13 12 11 7
第二圈8 9 10
每一圈都从右，下，左，上，当上下左右有元素时打印，当某个方向没有元素时，说明打印完了
圈数start = ceil(min(W,H)/2)
四个角,沿着四个角打印每个圈即可
start,start       --->          start,w-start-1
    ^                                  V
H-start-1,start   <---          H-start-1,w-start-1
"""


def print_matrix_cloclwisely(arr):
    start = 0
    while len(arr)>start*2 and len(arr[0])>start*2:
        print_one_circle(arr, start)
        start += 1

def print_one_circle(arr, start):
    for i in range(start, len(arr[0])-start):
        print(arr[start][i])
        
    if len(arr)-1-start>start:
        for i in range(start+1, len(arr)-start-1):
            print(arr[i][len(arr[0])-1-start])
        
    if len(arr[0])-1-start>start and len(arr)-1-start>start:
        for i in range(len(arr[0])-start-1, start, -1):
            print(arr[len(arr)-start-1][i])
    
    if len(arr)-1-start>start and len(arr)-1-start>start:
        for i in range(len(arr)-1-start, start, -1):
            print(arr[i][start])

arr = [[j*5+i for i in range(5)] for j in range(3)]
print_matrix_cloclwisely(arr)

    