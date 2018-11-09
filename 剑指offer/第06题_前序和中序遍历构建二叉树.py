# -*- coding:utf-8 -*-
"""
剑指offer第6题
问题：输入二叉树的前序遍历与中序遍历的结果，重建二叉树，假设前序遍历与中序遍历中都不包含重复元素
思路：递归
"""


class Queue:
    def __init__(self, max_size):
        self.arr = [0]*max_size
        self.curr_size = 0
        self.front = 0
        self.rear = -1
        
    def insert(self, value):
        self.rear += 1
        self.arr[self.rear] = value
        self.curr_size += 1
    
    def pop(self):
        self.curr_size -= 1
        value = self.arr[self.front]
        self.front += 1
        return value
    
    def is_empty(self):
        return self.curr_size == 0


class Node:
    def __init__(self, value):
        self.value = value
        self.left_node = None
        self.right_node = None


def construct_core(pre_order, in_order):
    if pre_order is None or in_order is None:
        return None
    for i in range(len(in_order)):
        if in_order[i] == pre_order[0]:
            root = Node(in_order[i])
#             print(root.value)
            root.left_node = construct_core(pre_order[1:i+1], in_order[:i])
            root.right_node = construct_core(pre_order[i+1:len(pre_order)], in_order[i+1:len(pre_order)])
            return root

# 层级遍历
def level_display(node):
    q = Queue(20)
    q.insert(node)
    while not q.is_empty():
        node = q.pop()
        print(node.value, end=" ")
        if node.left_node is not None:
            q.insert(node.left_node)
        if node.right_node is not None:
            q.insert(node.right_node)
        

pre_order = [1,2,4,7,3,5,6,8]
in_order = [4,7,2,1,5,3,8,6]
root = construct_core(pre_order, in_order)
level_display(root)          