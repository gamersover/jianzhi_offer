# -*- coding:utf-8 -*-
"""
剑指offer第4题
问题：实现一个函数，把字符串中的空格替换成"%20"
思路：读原字符串中的每个字符，如果读到空格，就添加"%20"
"""

def replace_blank(raw_str):
    replaced_str = ""
    for item in raw_str:
        if item == " ":
            replaced_str += "%20"
        else:
            replaced_str += item
    return replaced_str

if __name__ == "__main__":
    print(replace_blank("We are happy."))