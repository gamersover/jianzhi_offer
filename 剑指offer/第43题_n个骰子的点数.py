# -*- coding:utf-8 -*-
"""
剑指offer第43题
问题：把n个骰子扔在地上，所有骰子朝上一面的点数之和为s，输入n，打印出s
的所有可能的值出现的概率
思路：动态规划，假设已经知道前面n-1个骰子的总和，那么下一个骰子可能是1~6，相加就是n个骰子的点数
设dp[n][k]表示n个骰子的和为k的所有个数
当你n<=k<n+5时
dp[n][k] = dp[n-1][n-1] + .. + dp[n][k-1]
当n+5<=k<=6n时
dp[n][k] = dp[n-1][k-6] + ... + dp[n-1]dp[min(6n-6,k-1)]
小技巧，由于计算n个骰子的点数只需要用到n-1个骰子的点数，所以只用两个数组即可
一个数组存储n-1，另一个数组存储n
使用flag标记，比如flag=0表示第一个数组存储1,当flag=1表示第二个数组存储2，
当要存储3时，让flag=0表示第一个数组存储3，别忘记在存储3时，清0原数组，这样交替即可
"""

def get_all_sum(n):
    dp = [[0]*(n*6+1), [0]*(n*6+1)]
    flag = 0
    for i in range(1,7):
        dp[flag][i] = 1
    
    for j in range(2, n+1):
        
        for k in range(j, j+5):
            dp[1-flag][k] = 0
            for m in range(j-1, k):
                dp[1-flag][k] += dp[flag][m]
                
        for k in range(j+5, 6*j+1):
            end = min([6*j-6, k-1])
            dp[1-flag][k] = 0
            for m in range(k-6, end+1):
                dp[1-flag][k] += dp[flag][m]
        flag = 1- flag
    
    for i in range(n, 6*n+1):
        print(dp[flag][i])

get_all_sum(3)
        
        