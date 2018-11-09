# -*- coding:utf-8 -*-
"""
剑指offer第21题
问题：定义栈的数据结构，实现一个能够得到栈的最小元素的min函
调用min,push,pop时间复杂度都是O(1)
思路：直接用两个栈，一个存储元素，一个存储当前最小值，
比如 4 5 2 3 6 1
元素栈4 5 2 3 6 1
最小栈4 4 2 2 2 1
当pop时，两个栈同时pop,元素栈top永远是压入的元素，最小栈top永远是当前最小值
"""

class Stack:
    def __init__(self, max_size):
        self.top = 0
        self.max_size = max_size
        self.arr = [0]*max_size
    
    def push(self, data):
        self.arr[self.top] = data
        self.top += 1
    
    def pop(self):
        self.top -= 1
        return self.arr[self.top]
    
    def lenght(self):
        return self.top
    
    def peek(self):
        return self.arr[self.top-1]

class Stack2:
    def __init__(self, max_size):
        self.max_size = max_size
        self.min_stack = Stack(max_size)
        self.data_stack = Stack(max_size)
    
    def push(self, data):
        self.data_stack.push(data)
        if self.min_stack.lenght() == 0:
            self.min_stack.push(data)
        elif data < self.min_stack.peek():
            self.min_stack.push(data)
        else:
            self.min_stack.push(self.min_stack.peek())
    
    def pop(self):
        self.min_stack.pop()
        return self.data_stack.pop()
    
    def min(self):
        return self.min_stack.peek()

stack = Stack2(10)
stack.push(4)
stack.push(5)
stack.push(2)
stack.push(3)
stack.push(1)
stack.push(6)
print(stack.pop())
stack.pop()
stack.push(0)
print(stack.min())