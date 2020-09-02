def run():
    N, M = [int(x) for x in input().split()]
    data = []
    for _ in range(N):
        tmp= [int(x) for x in input().split()]
        if tmp[0] > 0 and tmp[1] < 0:
            continue
        data.append(tmp)
    N = len(data)
    dp = [[0]*M for _ in range(N)] 
    # print(data)
    # dp[i][j] 表示的是前i件物品中，背包为M的所能获取的最大价值
    # dp[i][j] = max(dp[i-1][j], dp[i-1][j-data[i][0]] + data[i][1])
    for j in range(M):
        if j >= data[0][0]:
            dp[0][j] = data[0][1]
    for i in range(1, N):
        for j in range(M):
            if j >= data[i][0]:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-data[i][0]]+ data[i][1])
            else:
                dp[i][j] = dp[i-1][j]
    print(dp[-1][-1])
    return
    

run()
        