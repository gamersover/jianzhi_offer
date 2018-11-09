# -*- coding:utf-8 -*-
"""
剑指offer第5题：
问题：输入一个链表的头结点，从尾到头放过来打印出每个节点的值
思路：可以利用栈，也可以使用递归
"""

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkList:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        current_node = self.root
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
    
    def display_forward(self):
        current_node = self.root
        while current_node is not None:
            print(current_node.value, end=" ")
            current_node = current_node.next
        print()
    
    def display_backward(self, node):
        if node is not None:
            if node.next is not None:
                self.display_backward(node.next)
            print(node.value, end=" ")
            

link_list = LinkList()
link_list.insert(100)
link_list.insert(80)
link_list.insert(70)
link_list.insert(20)
link_list.display_forward()
link_list.display_backward(link_list.root)
        
    
    
        