# -*- coding:utf-8 -*-
"""
剑指offer第25题
问题：输入一个二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所有路径，
从树的根结点开始往下一直到叶子结点所经过的路径形成一条路径
思路：递归
从根结点开始，将当前的路径压入栈中，并记下当前和，如果当前的和等于该整数，则打印栈内的路径，
如果不等于，对左右子树递归调用，并把当前和与栈传入，
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Stack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.top = 0
        self.arr = [0]*max_size
     
    def push(self, data):
        self.arr[self.top] = data
        self.top += 1
     
    def pop(self):
        self.top -= 1
        return self.arr[self.top]

def find_path(root, sum):
    if root is None:
        return False
    stack = Stack(10)
    curr_sum = 0
    find_sum_path(root, sum, stack, curr_sum)

def find_sum_path(root, sum, stack, curr_sum):
    curr_sum += root.data
    stack.push(root.data)
    if root.left is None and root.right is None:
        if curr_sum == sum:
            print("find")
            print(stack.arr[:stack.top])
    if root.left is not None:
        find_sum_path(root.left, sum, stack, curr_sum)
    if root.right is not None:
        find_sum_path(root.right, sum, stack, curr_sum)
    stack.pop()

root = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(5)
fifth = Node(7)
sixth = Node(4)
root.left = second
root.right = third
second.left = fourth
second.right = fifth
third.left = sixth
find_path(root, 8)
    