# -*- coding:utf-8 -*-
"""
剑指offer第27题
问题：输入一颗二叉搜索树，将该树转换成一个排序的双向链表。要求不能创建任何新的结点，
只能调整树中结点指针的指向
思路：递归，先完成左子树，使得左子树中的每个结点的右指针指向比它大的数，左指针指向比它小的数，
并获得左子树的最大结点即双向链表往右走的最后一个节点，在递归完成右子树，
最后可以得到整个双向链表往右走的最后一个结点
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
        
def convert(root):
    last_node = None
    last_node = convert_node(root, last_node)
    while last_node is not None and last_node.left is not None:
        last_node = last_node.left
    return last_node

def convert_node(root, last_node):
    if root is None:
        return
    current = root
    
    if current.left is not None:
        last_node = convert_node(current.left, last_node)
    current.left = last_node
    
    if last_node is not None:
        last_node.right = current
    
    last_node = current
    if current.right is not None:
        last_node = convert_node(current.right, last_node)
    return last_node

if __name__ == "__main__":
    root = Node(4)
    node1 = Node(2)
    node2 = Node(6)
    node3 = Node(1)
    node4 = Node(3)
    node5 = Node(5)
    node6 = Node(7)
    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4
    node2.left = node5
    node2.right = node6
    head = convert(root)
    print(head.data)
