# -*- coding:utf-8 -*-
"""
剑指offer第37题
问题：输入两个链表，找出它们的第一个公共结点
思路：从公共结点开始，后面两个链表肯定是一样的，
1->2->3->6->7->9->10-------
      4->5->7--------------
从7开始，两个链表后面一模一样，所以两个链表第一个相同的结点肯定不可能是1 2，从第3个结点开始比较即可
长链表的长度减去短链表的长度得到的差为起始寻找位置
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    

def get_first_common(head1, head2):
    len1 = get_len(head1)
    len2 = get_len(head2)
    dif = 0
    if len1 > len2:
        dif = len1 - len2
        long_list_node = head1
        short_list_node = head2
    else:
        dif = len2 - len1
        long_list_node = head2
        short_list_node = head1
    
    for i in range(dif):
        long_list_node = long_list_node.next
    
    while long_list_node != short_list_node and \
          long_list_node is not None and \
          short_list_node is not None:
        long_list_node = long_list_node.next
        short_list_node = short_list_node.next
    
    return long_list_node

def get_len(head):
    length = 0
    point = head
    while point is not None:
        point = point.next
        length += 1
    return length

if __name__ == "__main__":
    head1 = Node(1)
    second1 = Node(2)
    third1 = Node(3)
    forth1 = Node(6)
    fifth = Node(7)
    sixth = Node(9)
    seventh = Node(10)
    head2 = Node(4)
    second2 = Node(5)
    head1.next = second1
    second1.next = third1
    third1.next = forth1
    forth1.next = fifth
    fifth.next = sixth
    sixth.next = seventh
    head2.next = second2
    second2.next = fifth
    print(get_first_common(head1, head2).data)
        