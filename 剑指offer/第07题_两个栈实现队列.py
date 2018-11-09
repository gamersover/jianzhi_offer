#-*- coding:utf-8 -*-
"""
剑指offer第7题
问题：使用两个栈实现队列，appendTail在队列尾插入节点，pop删除头结点
思路：使用两个栈
"""
class Stack:
    
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.arr = [0]*self.maxsize
        self.top = 0

    def isEmpty(self):
        return self.top == 0

    def getSize(self):
        return self.top

    def pop(self):
        self.top = self.top - 1
        temp = self.arr[self.top]
        return temp

    def push(self, elem):
        self.arr[self.top] = elem
        self.top = self.top + 1


class Queue:

    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.stack1 = Stack(maxsize)
        self.stack2 = Stack(maxsize)

    def appendtail(self, elem):
        self.stack1.push(elem)

    def pop(self):
        if not self.stack2.isEmpty():
            return self.stack2.pop()

        else:
            while not self.stack1.isEmpty():
                temp = self.stack1.pop()
                self.stack2.push(temp)
            return self.stack2.pop()

    def isEmpty(self):
        return self.stack1.isEmpty() and self.stack2.isEmpty()

q = Queue(20)
q.appendtail(2)
q.appendtail(10)
q.appendtail(18)
q.appendtail(40)

print(q.pop())

q.appendtail(50)

while not q.isEmpty():
    print(q.pop())