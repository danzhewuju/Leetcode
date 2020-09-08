'''
测试用例
（][()）

1. 解题思路 动态规划 
dp[i][j]: 表示的是字符串s[i:j]的长度中最长的无法消除的子串
转移方程：dp[i][j] = dp[i][j-1]+1 or min(dp[i][j], dp[i][k-1]+dp[k+1][j-1])

'''

s = input()
length = len(s)
dp = [[0]*(length+1) for _ in range(length+1)]
for i in range(length):
    dp[i][i] = 1
for j in range(length):
    for i in range(j+1):
        dp[i][j] = dp[i][j-1] + 1  # 首先添加了一个字符
        for k in range(i, j):
            if ord(s[j]) - ord(s[k]) == 1 or ord(s[j]) - ord(s[k]) == 2:
                dp[i][j] = min(dp[i][j], dp[i][k-1]+dp[k+1][j-1])

print(dp[0][length-1])




# s = input()
# # s = '(][())'
# len = len(s)
# dp = [[0] * 200 for _ in range(200)]
# for i in range(len):
#     dp[i][i] = 1
# for i in range(len):
#     for j in range(i+1):
#         dp[j][i] = dp[j][i-1]+1
#         for k in range(j,i):
#             if ord(s[k])+1 == ord(s[i]) or ord(s[k])+2 == ord(s[i]):
#                 dp[j][i] = min(dp[j][i], dp[j][k-1] + dp[k+1][i-1])
# print(dp[0][len-1])