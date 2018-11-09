# -*- coding:utf-8 -*-
"""
剑指offer第40题：
问题：一个整形数组里除了两个数字之外，其他的数字都出现了两次。请写出程序找到这两个只
出现一次的数字。要求时间复杂度为O(n)，空间复杂度为O(1)。
思路：所有数字异或后的结果一定不为0，比如在2，4，3，6，3，2，5，5中最后异或的结果肯定是
4^6=0010的结果，可以看到倒数第二位为1，表示两个只出现一次的数的倒数第二位肯定不相同；
根据倒数第二位，将原数组分为两组，可以知道4和6肯定出现在不同的组，而且这两个组中，只有4和6出现过一次，
可以分别对这两个组求异或，两个组的结果就是两个出现一次的数
"""

def find_appear_once(arr):
    result = 0
    for item in arr:
        result ^= item
    index = find_bit_1(result)
    number1 = 0
    number2 = 0
    for item in arr:
        if is_bit_1(item, index):
            number1 ^= item;
        else:
            number2 ^= item;
    print(number1, number2)

def find_bit_1(result):
    index = 0
    while (result & 1)==0:
        result = result >> 1
        index += 1
    return index

def is_bit_1(number, index):    
    return (number>>index & 1)==1   

if __name__ == "__main__":
    arr = [2,4,3,6,3,2,5,5,4,0]
    find_appear_once(arr)