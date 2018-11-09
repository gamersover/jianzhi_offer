# -*- coding:utf-8 -*-
"""
剑指offer第38题
问题：统计一个数字在排序数组中出现的次数
思路：获得数字第一次出现的位置，和最后一次出现的位置，然后相减+1即可，得到
第一次出现的位置和最后一次出现的位置可以用折半查找法
"""

def get_fist(arr, k):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == k:
            if mid == 0 or (mid > 0 and arr[mid-1] != k):
                return mid
            else:
                end = mid - 1
        elif arr[mid] > k:
            end = mid - 1
        else:
            start = mid + 1
    return -1

def get_last(arr, k):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == k:
            if mid == end or (mid < end and arr[mid+1] != k):
                return mid
            else:
                start = mid + 1
        elif arr[mid] < k:
            start = mid + 1
        else:
            end = mid - 1
    return -1 

def get_number(arr, k):
    last = get_last(arr, k)
    first = get_fist(arr, k)
    if last > -1 and first > -1:
        return get_last(arr, k) - get_fist(arr, k) + 1
    else:
        return 0            
if __name__ == "__main__":
    arr = [1,2,3,3,3,3,4,5]
    k = 3
    print(get_number(arr, k))
             