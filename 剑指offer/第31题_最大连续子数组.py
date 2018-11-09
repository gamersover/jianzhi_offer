# -*- coding:utf-8 -*-
"""
剑指offer第31题
问题：
    求连续子数组之和最大的值
思路：
 从左到右计算前n项和,记住当前总和，如果总和小于0，就从第n+1项开始重新计和，并记录遇到过的最大值
"""

def maxsum_subarr(arr):
    maxsum = 0
    cursum = 0
    for i in range(len(arr)):
        if cursum<=0:
            cursum = arr[i]
        else:
            cursum += arr[i]
        if(cursum > maxsum):
            maxsum = cursum
    return maxsum

if __name__ == "__main__":
    arr = [-2,4,5,-2,5,-7,6,3,-1]
    print(maxsum_subarr(arr))
