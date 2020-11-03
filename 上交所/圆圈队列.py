def run():
    N, S = map(int, input().split())
    dp = [1]*(N+1)
    for i in range(2, S+1): # 第i个命令
        for j in range(1, N+1):
            if j % i == 0:
                dp[j] = abs(1-dp[j])
    res = [str(i+1) for i, d in enumerate(dp[1:]) if d == 1]
    print(" ".join(res))
    return 

run()