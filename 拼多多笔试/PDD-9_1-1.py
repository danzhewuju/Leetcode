def run():
    n = int(input())
    dp = [[0]*n for _ in range(n)]
    mid = n // 2
    # 2-3
    for i in range(mid):
        for j in range(mid):
            if i > j: 
                dp[i][j] = 3
            elif i < j:
                dp[i][j] = 2
    #1-8
    for i in range(mid):
        for j in range(mid, n):
            if i > n-1-j:
                dp[i][j] = 8
            elif i < n-1-j:
                dp[i][j] = 1
    # 4-5
    for i in range(mid, n):
        for j in range(mid):
            if i > n-1-j:
                dp[i][j] = 5
            elif i < n-1-j:
                dp[i][j] = 4
    #6-7
    for i in range(mid, n):
        for j in range(mid, n):
            if i > j:
                dp[i][j] = 6
            elif i < j:
                dp[i][j] = 7
    
    if n % 2 ==1:
        mid = n // 2
        for i in range(n):
            dp[mid][i] = 0
            dp[i][mid] = 0
    
    for i in range(n):
        tmp = [str(x) for x in dp[i]]
        print(" ".join(tmp))
    return 


run()


