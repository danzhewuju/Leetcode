def run():
    n, m, k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    a = [0]+a
    d = []
    dp = [[0]*(n+1) for _ in range(n+1)]  # 构建状态转移方程
    # dp[i-1][j] = dp[i][j]+K
    for i in range(n, 1, -1):
        for j in range(i+1, n+1, -1):
            if j - i < 2:
                if a[i]*a[j]+a[i]+a[j] == k:
                    dp[i][j] = 1
            else:
                count = 0
                for t in range(i, j+1):
                    try :
                        if a[i-1] * a[t] + a[t] + a[i-1] == k:
                            count += 1
                    except:
                        print(t, i)
                        # exit
                dp[i-1][j] = dp[i][j] + count
    min_=1000000
    max_=0 
    for i in range(m):
        tmp = [int(x) for x in input().split()]
        min_ = min(min_, min(tmp))
        max_ = max(max_, max(tmp))
        d.append(tmp)
    for l, r in d:
        print(dp[l][r])
        # print(ans)
if __name__ == "__main__":
    run()
    pass