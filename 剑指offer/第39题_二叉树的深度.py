# -*- coding:utf-8 -*-
"""
剑指offer第39题
问题：输入一颗二叉树的根结点，求该树的深度。从根结点到叶结点依次经过的结点形成的一条路径，最长
路径的长度为树的深度
思路：递归，获取左子树的长度，右子树的长度，返回长度长的那个+1
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def get_depth(root):
    if root is None:
        return 0
    
    left_depth = get_depth(root.left)
    right_depth = get_depth(root.right)
    if left_depth > right_depth:
        return left_depth + 1
    else:
        return right_depth + 1

if __name__ == "__main__":
    root = Node(2)
    node1 = Node(3)
    node2 = Node(4)
    root.left = node1
    root.right = node2
    node3 = Node(5)
    node4 = Node(6)
    node1.left = node3
    node3.right = node4
    print(get_depth(root))