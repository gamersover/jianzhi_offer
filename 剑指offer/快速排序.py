# -*- coding:utf-8 -*-

# 不含相同元素的快速排序
def quick_sort(a):
    if len(a) <= 1:
        return a
    mid = a[0]
    left = [j for j in a if j<mid]
    right = [j for j in a if j>mid]
    return quick_sort(left) + [mid] + quick_sort(right)

# 含相同元素的快速排序
def quick_sort_2(a):
    if len(a) <= 1:
        return a
    mid = a[0]
    left = [j for j in a if j<mid]
    right = [j for j in a if j > mid]
    mid_ = [j for j in a if j==mid]
    return quick_sort_2(left) + mid_ + quick_sort_2(right)


a = [4,1,1,5,2,6,10,3]
print(quick_sort_2(a))