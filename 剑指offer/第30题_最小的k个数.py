# -*- coding:utf-8 -*-
"""
剑指offer第30题
问题：输入n个整数，找出其中最小的k个数
思路：定义k大小的容器，循环以下步骤：
记住当前容器中的最大值，每来一个新元素，和最大值对比，如果该元素大于最大值，
则不放进容易，如果小于最大值，将最大值与新元素交换。
扩展:使用最大堆来作为该容器
"""

def get_least_numbers(arr, k):
    least_arr = arr[:k]
    for i in range(k, len(arr)):
        max_ptr = least_arr.index(max(least_arr))
        if arr[i] < arr[max_ptr]:
            least_arr[max_ptr] = arr[i]
    return least_arr

if __name__ == "__main__":
    arr = [4,5,1,6,2,7,3,8]
    k = 4
    print(get_least_numbers(arr, k))
            