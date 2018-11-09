# -*- coding:utf-8 -*-
"""
剑指offer第18题
问题：输入两颗二叉树A和B,判断B是不是A子结构
思路：递归
主函数：先判断以A的根结点为B的各结点，是否有相同的子树，如果是则返回True,如果不是调用自身来
判断A根节点的左子树后者是右子树是否和B有相同的子树。
次函数：判断相同根节点是否有相同子树，首先看根节点是否相等，如果不等，返回False,如果相等，继续判断左边和右边子树的根节点是否
相等，一直下去，知道所有的节点都相等，返回True,一旦有一个不相等返回Fasle
所以,有两个递归
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def has_sub_tree(root1, root2):
    result = False
    if root1 is not None and root2 is not None:
        result = does_tree1_have_tree2(root1, root2)
        if not result:
            result = does_tree1_have_tree2(root1.left, root2)
            if not result:
                result = does_tree1_have_tree2(root1.right, root2)
    return result

def does_tree1_have_tree2(root1, root2):
    if root2 is None:
        return True
    elif root1 is None:
        return False
    if root1.data != root2.data:
        return False
    else:
        return does_tree1_have_tree2(root1.left, root2.left) and \
               does_tree1_have_tree2(root1.right, root2.right)

if __name__ == "__main__":
    root1 = Node(8)
    node1 = Node(8)
    node2 = Node(7)
    node3 = Node(9)
    node4 = Node(2)
    node5 = Node(4)
    node6 = Node(7)
    root1.left = node1
    root1.right = node2
    node1.left = node3
    node1.right = node4
    node2.left = node5
    node2.right = node6
     
    root2 = Node(8)
    a = Node(9)
    b = Node(2)
    root2.left = a
    root2.right = b
     
    print(has_sub_tree(root1, root2))

    