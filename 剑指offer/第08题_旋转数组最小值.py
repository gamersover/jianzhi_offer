# -*- coding:utf-8 -*-
"""
剑指offer第8题
问题：
 把一个数组最开始的若干元素搬到数组的末尾，我称之为数组的旋转。
 输入一个递增排序的数组的一个旋转，输出旋转数组的最小值。
思路：
 一般情况[5,1,2,3,4]
 定义左右指针，取中点mid，
  1.如果右边的数小于左边，且右边的index减去左边的index等于，右边的值就是最小值
  2.如果中间值小于左边的值，说明最小值在左边，让right=mid
  3.如果中间值大于右边的值，说明最小值在右边，left=mid
特殊情况：[1,0,1,1,1]和[1,1,1,1,1]，如果左边的值等于右边的值等于中间的值，left+1, right-1。
"""
def get_rotate_min(arr):
    left = 0
    right = len(arr) - 1
    while arr[left] >= arr[right]:
        if right-left<=1:
            return arr[right]
        mid = (left+right) // 2
        if arr[mid]==arr[left] and arr[mid]==arr[right]:               
            left += 1
            right -= 1
        elif arr[mid] < arr[left]:
            right = mid
        elif arr[mid] > arr[right]:
            left = mid
    return arr[left]
            

if __name__ == "__main__":
    arr = [2,3,4,5,1]
    arr1 = [7,7,7,7,5,6,7]   #剑指offer上的代码有问题，对于这种情况，它输出6
    print(get_rotate_min(arr1))