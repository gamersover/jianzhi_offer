# -*- coding:utf-8 -*-
"""
剑指offer第16题
问题：输入一个链表的头结点，反转该链表并输出反转后链表的头结点
思路：a->b->c->d
首先新的头结点new_head->a.next, a.next->new_head.next, 
new_head.next->curr_head, curr_head->new_head
上面四步实现方案：
new_head->b, a->c->d, b->a->c->d, curr_head->b
new_head->c, b->a->d, c->b->a->d, curr_head->c
new_head->d, c->b->a, d->c->b->a, curr_head->d
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
        
def reverse_list(node):
    if node is None:
        return None
    elif node.next is None:
        return node
    
    curr_head = node
    head = node
    while head.next is not None:
        new_head = head.next
        head.next = new_head.next
        new_head.next = curr_head
        curr_head = new_head
    return curr_head

if __name__ == "__main__":
    first = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)
    first.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    print(reverse_list(first).data)