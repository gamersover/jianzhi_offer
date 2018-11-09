# -*- coding:utf-8 -*-
"""
剑指offer第26题
问题：复制一个复杂链表，在复杂链表中，每个节点除了有一个next指针指向下一个结点外，
还有一个指向链表中任意结点或null的sibling指针
思路：分三步，第一步复制一个结点，然后复制结点指向原结点的next,再让原结点的next指向复制结点
第二步让原结点的next即（复制节点）的sibling结点指向原结点的sibling结点的next结点（sibling的复制结点）
第三步让原结点的next指向源节点的next的next
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.sibling = None

def copy_list(root):
    clone_nodes(root)
    connect_sibling_nodes(root)
    return reconnect_nodes(root)

def clone_nodes(root):
    node = root
    while node is not None:
        copy_node = Node(node.data)
        copy_node.next = node.next
        node.next = copy_node
        node = copy_node.next

def connect_sibling_nodes(root):
    node = root
    while node is not None:
        copy_node = node.next
        if node.sibling is not None:
            copy_node.sibling = node.sibling.next
        node = copy_node.next

def reconnect_nodes(root):
    node = root
    copy_root = node.next
    while node is not None:
        copy_node = node.next
        next_node = copy_node.next
        if next_node is not None:
            copy_node.next = next_node.next
        node = next_node
    return copy_root
        

if __name__ == "__main__":
    root = Node(0)
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    root.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    root.sibling = node2
    node2.sibling = root
    node4.sibling = node1
    copy_root = copy_list(root)
    print(copy_root)
    
        