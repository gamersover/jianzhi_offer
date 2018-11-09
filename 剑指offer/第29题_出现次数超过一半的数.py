# -*- coding:utf-8 -*-
"""
剑指offer第29题
问题：数组中有一个数字出现次数超过数组长度的一半，请找出这个数字
思路：这个数出现的次数肯定比其它数出现的次数加起来还多，
当遇到相同的数时，count+=1,当遇到不同的数时，count-=1，当count==0时，表示前面出现次数最多
的数的次数少于等于其它数出现次数的总和，那么后面的数组中，显然有出现最多的数的次数比后面中其它出现次数的总和
还有多，重置当前数，count重新+/-1即可
网友提供：
采用阵地攻守的思想：
第一个数字作为第一个士兵，守阵地；count = 1；
遇到相同元素，count++;
遇到不相同元素，即为敌人，同归于尽,count--；当遇到count为0的情况，又以新的i值作为守阵地的士兵，继续下去，到最后还留在阵地上的士兵，有可能是主元素。
再加一次循环，记录这个士兵的个数看是否大于数组一般即可。
"""

def more_than_half_num(arr):
    count = 0
    for item in arr:
        if count == 0:
            curr_num = item
            count = 1
        elif curr_num == item:
            count += 1
        else:
            count -= 1
    if check_more_than_half(arr, curr_num):
        return curr_num
    else:
        return None

def check_more_than_half(arr, number):
    times = 0
    for item in arr:
        if number == item:
            times += 1
    if times*2 <= len(arr):
        return False
    else:
        return True
arr = [1,2,3,2,2,2,5,4,2]
print(more_than_half_num(arr))