# -*- coding:utf-8 -*-

# 二叉搜索树python实现
# 插入，删除，查找，遍历
class Node:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

    def displayNode(self):
        print(self.data, end=' ')

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        newNode = Node(data)
        if self.root is None:
            self.root = newNode

        else:
            current = self.root
            while True:
                parent = current
                if data < current.data:
                    current = current.lchild
                    if current is None:
                        parent.lchild = newNode
                        return
                else:
                    current = current.rchild
                    if current is None:
                        parent.rchild = newNode
                        return

    def delete(self, data):
        current = self.root
        while current.data != data:
            parent = current
            if current.data > data:
                current = current.lchild
                islchild = True
            else:
                current = current.rchild
                islchild = False
            if current is None:
                return False

        if current.lchild is None and current.rchild is None:
            if current == self.root:
                self.root = None
            elif (islchild):
                parent.lchild = None
            else:
                parent.rchild = None

        elif current.lchild is None:
            if current == self.root:
                self.root = current.rchild
            elif (islchild):
                parent.lchild = current.rchild
            else:
                parent.rchild = current.rchild

        elif current.rchild is None:
            if current == self.root:
                self.root = current.lchild
            elif (islchild):
                parent.lchild = current.lchild
            else:
                parent.rchild = current.lchild

        else:
            successor = self.getSuccessor(current)
            if current == self.root:
                self.root = successor
            elif (islchild):
                parent.lchild = successor
            else:
                parent.rchild = successor
            successor.lchild = current.lchild

    def getSuccessor(self, node):
        current = node.rchild
        successorParent = node
        successor = node
        while current is not None:
            successorParent = successor
            successor = current
            current = current.lchild
        if successor != node.rchild:
            successor.lchild = successor.rchild
            successor.rchild = node.rchild
        return successor

    def find(self, data):
        current = self.root
        while (current.data != data) and current is not None:
            if current.data > data:
                current = current.lchild
            else:
                current = current.rchild

        return current

    def preOrder(self, node):
        if node is not None:
            node.displayNode()
            self.preOrder(node.lchild)
            self.preOrder(node.rchild)

    def inOrder(self, node):
        if node is not None:
            self.inOrder(node.lchild)
            node.displayNode()
            self.inOrder(node.rchild)

    def postOrder(self, node):
        if node is not None:
            self.postOrder(node.lchild)
            self.postOrder(node.rchild)
            node.displayNode()

    def travese(self, type):
        if type == 'inorder':
            self.inOrder(self.root)
        elif type == 'postorder':
            self.postOrder(self.root)
        else:
            self.preOrder(self.root)
        print("")

bt = BinaryTree()

bt.insert(100)
bt.insert(20)
bt.insert(10)
bt.insert(120)
bt.insert(30)
bt.insert(40)
bt.insert(2)

bt.travese(type='preorder')

bt.delete(100)
bt.travese(type='pretorder')