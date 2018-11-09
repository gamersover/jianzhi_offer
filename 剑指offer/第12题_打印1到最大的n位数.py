# -*- coding:utf-8 -*-
"""
剑指offer第12题
问题：输入数字n，按顺序打印1到最大的n位进制数
思路：n太大时，暴力法不好，可以考虑求n位数的全排列，然后把前面的0不打印
全排列递归思路：首先固定最高位，然后全列剩下的——固定当前最高位，当位数超过n时，即排列好了一个数，再打印
"""

def print_to_max(n):
    if n <= 0:
        return
    arr = [0]*n
    print_arr(arr, 0)

def print_arr(arr, n):
    for i in range(10):
        # 先固定第n位，这里最高位即第0位
        if n != len(arr):
            arr[n] = i
            print_arr(arr, n+1)
        # 当n达到len(arr)，即排列完一个数后，打印这个数
        else:
            flag = False          # 用来标记是否遇到了第一个不为0的数 
            for j in range(len(arr)):
                if arr[j] != 0:
                    print(arr[j], end="")
                    if not flag:
                        flag = True
                else:
                    if flag:      # 遇到了第一个不为0的数，那么后面的都可以打印
                        print(arr[j], end="")
            if flag:                # 表示遇到了不为0的数，即不是全0的数，打印换行
                print()             # 如果是全0的数，什么都不打印
            return

print_to_max(2)
                    
                    
                
                
        
    