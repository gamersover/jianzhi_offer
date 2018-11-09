# -*- coding:utf-8 -*-
"""
剑指offer第36题
问题：在数组中的两个数如果前一个数字大于后一个数字，则这两个数字组成一个逆序对，输入
一个数组，求出这个数组的逆序对的总数
思路：
思路1：使用冒泡排序，交换次数就是逆序对的总数
思路2：使用归并排序，得到排序后的数组，已经逆序数，假设左边和右边已经排好序了，且逆序数left和right都知道
现在需要计算左右之间的逆序数
左边有序5 7    右边 有序4 6
1.先比较7和6，如果7比6大，那么7一定比4大，则将7为排好序的最后一个元素，且逆序数为右边的长度
2.在比较5和6，如果5小于6，那么排好序的倒数第二个数一定是6，这个时候没有逆序数，右边指针指向4
3.在比较5和4，如果5大于4，和1一样处理，5是倒数第三个数，且逆序数为现在右边的指针-右边开始的指针
归并排序先取最大值的步骤和求逆序数的步骤一样！！
"""
# 思路1
def get_inverse_pairs(arr):
    count = 0
    for i in range(len(arr)-1):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                count += 1
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return count

# 思路2
def get_inverse_pairs2(arr):
    start = 0
    end = len(arr) - 1
    temp = [0]*len(arr)
    return merge_sort(arr, start, end, temp)

def merge_sort(arr, start, end, temp):
    """
    temp用来存储排好序的数组，下一次递归，将排好序的数组传给arr
    """
    if start == end:
        temp[start] = arr[start]
        return 0
    mid = (end - start) // 2
    left = merge_sort(temp, start, start+mid, arr)
    right = merge_sort(temp, start+mid+1, end, arr)
    count = 0
    left_index = start+mid
    right_index = end
    point = end
    while left_index >= start and right_index >= start+mid+1:
        if arr[left_index] > arr[right_index]:
            count += right_index - (start+mid)
            temp[point] = arr[left_index]
            left_index -= 1
            point -= 1
                
        elif arr[left_index] < arr[right_index]:
            temp[point] = arr[right_index]
            right_index -= 1
            point -= 1
    # 左边或右边没有元素后的清理
    for i in range(left_index, start-1, -1):
        temp[point] = arr[i]
        point -= 1
    for j in range(right_index, start+mid, -1):
        temp[point] = arr[j]
        point -= 1
    return count+left+right

if __name__ == "__main__":
    arr = [7,5,6,4]
    print(get_inverse_pairs2(arr))