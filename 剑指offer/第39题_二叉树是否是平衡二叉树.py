# -*- coding:utf-8 -*-
"""
剑指offer第39题2
问题：输入一颗二叉树的根结点，判断该树是不是平衡二叉树，如果某二叉树中的
任意结点的左右子树的深度相差不超过1，那么它就是一颗平衡二叉树
思路：递归，判断左右子树的高度差是否不超过1，再判断左右子树是否是平衡二叉树,
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def is_balanced(root):
    if root is None:
        return True
    left_depth = get_depth(root.left)
    right_depth = get_depth(root.right)
    if abs(left_depth - right_depth) > 1:
        return False
    else:
        return is_balanced(root.left) and is_balanced(root.right) 

def get_depth(root):
    if root is None:
        return 0
    left_depth = get_depth(root.left)
    right_depth = get_depth(root.right)
    return 1 + (left_depth if left_depth>right_depth else right_depth)

# def is_balanced_recursive(root, depth):
#     if root is None:
#         depth = 0
#         return True
#     left, right = 0, 0
#     if is_balanced_recursive(root.left, left) and \
#         is_balanced_recursive(root.right, right):
#         diff = right - left
#         if diff <= 1 and diff >= -1:
#             if left > right:
#                 depth = 1 + left
#             else:
#                 depth = 1 + right
#             return True
#     return False

if __name__ == "__main__":
    root = Node(2)
    node1 = Node(3)
    node2 = Node(4)
    root.left = node1
    root.right = node2
    node3 = Node(5)
    node4 = Node(6)
    node1.left = node3
    node3.right = node4
    print(is_balanced(root))
