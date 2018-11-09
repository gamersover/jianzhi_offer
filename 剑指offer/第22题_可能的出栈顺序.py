# -*- coding:utf-8 -*-
"""
剑指offer第22题
问题：输入两个整数序列，第一个序列表示栈的压入顺序，判断第二个序列是否为该栈的出栈序列
假设所有压入的数字均不相等, 所有可能的出栈序列一共有C(2n,n)/(n+1) 查看卡特兰数
思路：
使用两个指针和一个栈
比如 a b c d e f g h
   f h e d c b a g
p1指针指向压入顺序的开头，p2指针指向出栈序列的开头
p2指针先指向出栈f,然后使用p1指针让a b c d e f依次压入栈中，然后p1指针指向入栈f
p1指的数与p2指向的数相等，f出栈,栈中还有a b c d e,这是p2指针指向出栈h，p1指针指向入栈g
同理使用p1指针使得g h入栈，栈中a b c d e g h，p1指向入栈h，p2指向出栈h
这是相同h出栈,栈中a b c d e g,p2指向出栈e,此时p1不指向数，而栈顶元素与p2指向的元素不相同，
所以该序列不是出栈序列
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
    
    def is_empty(self):
        return self.top == 0
    
def is_pop_order(arr1, arr2):
    p1 = 0
    stack = Stack(len(arr1))
    for i in range(len(arr2)):
        if not stack.is_empty() and stack.peek() == arr2[i]:
            stack.pop()
        else:
            if p1 == len(arr1):  # 表示arr2中的数不在arr1中
                return False
            else:
                while True:
                    stack.push(arr1[p1])
                    p1 += 1
                    if stack.peek() == arr2[i] or p1 == len(arr1):
                        break
                if stack.peek() == arr2[i]:
                    stack.pop()
                else:
                    return False
    return True

arr_1 = [1,2,3,4,5]
arr_2 = [1,2,3,4,5]
print(is_pop_order(arr_1, arr_2))  
    

