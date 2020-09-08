def run():
    n, a, b = [int(x) for x in input().split()]
    M = []  # 获得利润的二维矩阵, M[i][0]: 第i量车去a点赚取的钱，M[i][1]: 第i量车去B点赚的钱
    for i in range(n):
        x, y = [int(x) for x in input().split()]
        M.append([x, y])
    dp = [[[0]*(b+1) for _ in range(a+1)] for _ in range(n+1)]
    # 动态规划 dp的形状（n, a, b）
    # dp[i][k][t] : 表示的是 i量车，其中a地最多调度k 辆车， b地最多可调度t量车所能赚取的最大利润
    # 转移方程： dp[i][k][t] = max(dp[i-1][k-1][t]+M[i-1][0], dp[i-1][k][t-1]+M[i-1][1], dp[i-1][k][t])
    # 初始化操作
    for i in range(1, n+1):
        for k in range(a+1):
            for t in range(b+1):
                if k == 0 and t != 0: # a地没有需求
                    dp[i][k][t] = max(dp[i][k][t-1]+M[i-1][1], dp[i-1][k][t])
                elif k != 0 and t == 0: # b地没有需求
                    dp[i][k][t] = max(dp[i][k-1][t]+M[i-1][0], dp[i-1][k][t])
                elif k == 0 and t == 0: # 同时需求为0，没法赚钱
                    dp[i][k][t] = 0
                else:                # 一般情况
                    # 需要考虑到i 与 （k+t）的大小
                    dp[i][k][t] = max(dp[i-1][k-1][t]+M[i-1][0], dp[i-1][k][t-1]+M[i-1][1], dp[i-1][k][t]) 
    return dp[-1][-1][-1]

print(run())

    
    