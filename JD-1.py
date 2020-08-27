def run():
    n = int(input().strip())
    l = 2*n -1 # 表示的长度
    score = [[0]*l for _ in range(n)]
    for i in range(n):
        line = input().strip()
        tmp = [int(x) for x in line.split()]
        score[i] = tmp
    # print(score)
    dp = [[0]*(2*i-1) for i in range(1, n+1) ]
    # print(dp)
    dp[0][0] = score[0][0]
    for i in range(n-1):
        for j in range(len(score[i])):
            s = dp[i][j]
            dp[i+1][j] = max(dp[i+1][j], score[i+1][j]+s)
            dp[i+1][j+1] = max(dp[i+1][j+1], s+score[i+1][j+1])
            dp[i+1][j+2] = max(dp[i+1][j+2], s+score[i+1][j+2])
    # print(dp)
    print(max(dp[-1]))


while True:
    try:
        run()
    except:
        break
