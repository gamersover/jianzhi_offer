# -*- coding:utf-8 -*-
"""
剑指offer第17题
问题：输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的
思路：1->3->4->7, 2->3->5->8
两个指针p1,p2分别指向两个头结点，再比较两个头结点的值，取小的那个添加到新的链表中，然后那个指针指向下一个
步骤：
p->1, 3->4->7, 2->3->5->8
p->1->2, 3->4->7, 3->5->8
继续，直到某一个为空，结束
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# 非递归
def merge_list(head_1, head_2):
    # 确定头结点
    if head_1 is None:
        head = head_2
    elif head_2 is None:
        head = head_1
    else:
        if head_1.data <= head_2.data:
            head = head_1
            head_1 = head_1.next
        else:
            head = head_2
            head_2 = head_2.next
    
        curr_node = head
        while head_1 is not None and head_2 is not None:
            if head_1.data <= head_2.data:
                curr_node.next = head_1
                head_1 = head_1.next
            else:
                curr_node.next = head_2
                head_2 = head_2.next
            curr_node = curr_node.next
        if head_1 is None:
            curr_node.next = head_2
        elif head_2 is None:
            curr_node.next = head_1
    return head 

# 递归
def merge_list_recursive(head_1, head_2):
    if head_1 is None:
        return head_2
    elif head_2 is None:
        return head_1
    if head_1.data <= head_2.data:
        head = head_1
        head.next = merge_list_recursive(head_1.next, head_2)
    else:
        head = head_2
        head.next = merge_list_recursive(head_1, head_2.next)
    return head
        
    

if __name__ == "__main__":
    first_1 = Node(1)
    second_1 = Node(3)
    third_1 = Node(5)
    first_1.next = second_1
    second_1.next = third_1
    
    first_2 = Node(1)
    second_2 = Node(3)
    third_2 = Node(6)
    first_2.next = second_2
    second_2.next = third_2
    
    first = merge_list(first_1, first_2)
    current = first
    while current is not None:
        print(current.data, end=" ")
        current = current.next
        