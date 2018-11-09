#-*- coding:utf-8 -*-
'''
剑指offer第3题
一个二维数组， 每一行从左到右递增，每一列从上到下递增。输入一个二维数组和一个整数，判断数组中是否含有该整数。
----------
思路：先从第0列的最右边找，如果大于最右边那个数，说明在下一列，如果小于最右边那个数，后退一列，与该行的次大对比，
依此这个过程就可以找到了。

关键：先根据行当前的最大值定位到是哪一行
'''


def find(arr, number):
    row = 0
    column = len(arr[0]) - 1
    while(row < len(arr) and column > 0):
        if(arr[row][column]==number):
            return True
        elif(arr[row][column] > number):
            column -= 1
        else:
            row += 1
    return False

if __name__ == '__main__':
    arr = [[0 for i in range(4)] for j in range(4)]
    arr[0][0] = 1
    arr[0][1] = 3
    arr[0][2] = 8
    arr[0][3] = 9
    arr[1][0] = 2
    arr[1][1] = 4
    arr[1][2] = 9
    arr[1][3] = 12
    arr[2][0] = 4
    arr[2][1] = 7
    arr[2][2] = 10
    arr[2][3] = 13
    arr[3][0] = 6
    arr[3][1] = 8
    arr[3][2] = 15
    arr[3][3] = 17
    
    print(find(arr, 3))