# -*- coding:utf-8 -*-
"""
剑指offer第24题
问题：输入一个整数数组，判断该数组是不是某个二叉搜索树的后序遍历结果
思路：递归判断，按照左、右、中的顺序
比如5 7 6 9 11 10 8
8是根节点，比8小的（5,7,6）全在比8大（9,11,10）的左边
递归判断两个更小的数组
"""

def is_post_order(arr):
    if arr is None or len(arr) == 0:
        return False
    if len(arr) == 1:
        return True
    root = arr[-1]
    cut = 0
    for i in range(len(arr)-1):
        if arr[i] > root:
            cut = i + 1
            break
    if cut == 0:
        return is_post_order(arr[:-1])
    else:
        for j in range(cut, len(arr)):
            if arr[j] < root:
                return False
    left = True
    if cut > 0:
        left = is_post_order(arr[:cut])
    right = True
    if cut < len(arr) - 1:
        right = is_post_order(arr[cut-1:len(arr)-1])
    return left and right

arr = [5,7,6,9,11,10,8]
print(is_post_order(arr))