n, m = [int(x) for x in input().split()]
M, R = [], []
for i in range(n):
    x, y = [int(x) for x in input().split()]
    M.append(x)
    R.append(y)
# 0/1的背包问题, n: 个数  m: 最大的代价 M: 表示花费， R：表示获得总价值 dp[i][m]:表示的是前 i 个数最大花费所获得最大值
# dp(i, m) = max(dp(i-1, m-M[i])+R[i], dp(i-1, m))
dp = [[0]*(m+1) for _ in range(n)]
# 初始化
for i in range(m):
    if i >= M[0]:
        dp[0][i] = R[0]

for i in range(1, n):
    for j in range(1, m+1):
        if j < M[i]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-M[i]]+R[i])
print(dp[-1][-1])












