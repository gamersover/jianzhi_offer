# -*- coding:utf-8 -*-
"""
剑指offer第42题
问题：字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。
请定义一个函数实现字符串左旋转操作的功能。
比如输入字符串“abcdefg”和数字2.该函数左旋转2位得到的结果“cdefgab".
思路：将ab翻转，将cdefg翻转，得到bagfedc,再将整个翻转得到cdefgab
"""

def left_rotate_string(str, index):
    left_reverse = str[:index][::-1]
    right_reverse = str[index:][::-1]
    return (left_reverse+right_reverse)[::-1]

str_test = "abcdefg"
index = 2
print(left_rotate_string(str_test, index))