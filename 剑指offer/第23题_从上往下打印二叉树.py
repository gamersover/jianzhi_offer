# -*- coding:utf-8 -*-
"""
剑指offer第23题
问题：从上往下打印二叉树的每个节点，同一层的节点按照从左到右顺序打印
思路：利用队列实现，在前序和中序遍历构建二叉树中有
比如二叉树
    a
  b   c
 d e f g
a入队后，a出队并打印，a左右节点入队,这时队列中是b c
b出队并打印，b的左右节点入队，这时队列是c d e
c出队并打印，c的左右节点入队，这时队列是d e f g
d出队并打印，d没有左右节点，继续e出队并打印，依此类推
"""

class Queue:
    def __init__(self, max_size):
        self.head = 0
        self.rear = 0
        self.max_size = max_size
        self.arr = [0]*max_size
        
    def insert(self, data):
        self.arr[self.rear] = data
        self.rear += 1
    
    def pop(self):
        temp = self.arr[self.head]
        self.head += 1
        return temp
    
    def is_empty(self):
        return self.head == self.rear

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def print_by_level(root):
    if root is None:
        return None
    q = Queue(20)
    q.insert(root)
    while not q.is_empty():
        curr = q.pop()
        print(curr.data)
        if curr.left is not None:
            q.insert(curr.left)
        if curr.right is not None:
            q.insert(curr.right)

if __name__ == "__main__":
    head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)
    sixth = Node(6)
    head.left = second
    head.right = third
    second.left = fourth
    second.right = fifth
    third.left = sixth
    print_by_level(head)
        