def run():
    P = input()
    T = input()
    m, n = len(P), len(T)
    # 设置状态转移的数组
    dp = [[0] * n for _ in range(m)]
    # 状态转移方程 dp[i][j] = dp[i-1][j-1] # 此时是出现问号，或者是正常匹配的情况下
    # 初始条件设置
    i, j, star = 0, 0, 0
    if P[i] == '*':
        for t in range(n):
            dp[0][t] = 1
        t = 1
        while P[t] == '*':
            dp[t][0] = 1
            t += 1
        if t < m and P[t] == T[0] or P[t] == '?':
            dp[t][0] = 1
            t += 1
        while t < m and P[t] == '*':
            dp[t][0] = 1
            t += 1
        star += 1
    else:
        if P[i] == T[j] or P[i] == '?':
            dp[i][j] = 1
            i += 1
            j += 1
        else:
            print(0)
            exit()

    for i in range(1, m):
        if P[i] == '*':
            star += 1
            index = i - 1
            if 1 in dp[i - 1][i - star:]:
                flag = 1
                index = dp[i - 1][i - star:].index(1)
                index += i - star  # 找到i-star位置后面第一个匹配的位置
            else:
                flag = 0

            for t in range(index, n):
                dp[i][t] = flag
            continue
        for j in range(1, n):
            if P[i] == T[j] or P[i] == '?':
                dp[i][j] = dp[i - 1][j - 1]

    print(dp[-1][-1])


run()
