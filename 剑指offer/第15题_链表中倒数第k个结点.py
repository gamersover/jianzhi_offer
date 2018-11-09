# -*- coding:utf-8 -*-
"""
剑指offer第15题，输入一个链表，输出该链表中倒数第k个结点。比如说倒数第1个结点就是最后一个节点
思路：倒数第k个结点就是第n-k个结点(从0开始数),有(n-1) - (k-1) = (n-k) - 0
上式表示从头结点到n-k个结点经过的步数等于从k-1个结点到最后一个结点
首先找到第k-1个结点，然后用两个指针，一个(p1)指向头结点，一个(p2)指向k-1个结点，
两个指针同时移动,当p2到达最后一个结点时，p1到达了n-k个结点，即倒数第k个结点
""" 


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def find_to_tail(node, k):
    if node is None or k == 0:
        return None
    
    p2 = node
    for i in range(1, k):
        if p2.next is not None:
            p2 = p2.next
        else:
            return None
    p1 = node
    while p2.next is not None:
        p1 = p1.next
        p2 = p2.next
    return p1

head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
fifth = Node(5)
head.next = second
second.next = third
third.next = fourth
fourth.next = fifth

res_node = find_to_tail(head, 2)
print(res_node.data)
    