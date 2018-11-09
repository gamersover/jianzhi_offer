# -*- coding:utf-8 -*-
"""
剑指offer第13题
问题：在给定单向链表的头指针和一个结点指针，要求在O(1)时间内删除该结点
思路：由于是单向，如果查找到该结点的前一个节点，那时间复杂度是O(n),可以将该结点的
下个结点的数据复制给该节点，然后删除下一个结点
例如：1->2->3->4,删除3
1->3->3->4
1->3->4
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def delete_node(head, node):
    if node is head:      # 头结点，直接指向None
        head = None
    elif node.next is None: # 尾节点，只有遍历
        curr_node = head
        while curr_node.next.next is not None:
            curr_node = curr_node.next
        curr_node.next = None
    else:  # 中间节点
        node.data = node.next.data
        node.next = node.next.next


if __name__ == "__main__":
    head = Node(1)
    second = Node(2)
    third = Node(3)
    head.next = second
    second.next = third
    delete_node(head, second)
    print(head.next.data)
    
        
        