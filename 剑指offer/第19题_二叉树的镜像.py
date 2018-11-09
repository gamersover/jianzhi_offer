# -*- coding:utf-8 -*-
"""
剑指offer第19题
问题：输入一个二叉树，输出它的镜像
思路：递归 或者书中所用的栈
向交换左右子树，然后递归调用对左右子树镜像
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def mirror_tree(root):
    if root is None:
        return
    if root.left is not None or root.right is not None:
        root.left, root.right = root.right, root.left
        mirror_tree(root.left)
        mirror_tree(root.right)

def pre_order(root):
    if root is not None:
        print(root.data)
        pre_order(root.left)
        pre_order(root.right)

if __name__ == "__main__":
    root1 = Node(8)
    node1 = Node(8)
    node2 = Node(7)
    node3 = Node(9)
    node4 = Node(2)
    node5 = Node(4)
#     node6 = Node(7)
    root1.left = node1
    root1.right = node2
    node1.left = node3
    node1.right = node4
    node2.left = node5
#     node2.right = node6
    mirror_tree(root1)
    pre_order(root1)