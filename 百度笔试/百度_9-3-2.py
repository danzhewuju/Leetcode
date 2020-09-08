def run():
    n = int(input())
    graph = []
    for i in range(n):
        tmp = [int(x) for x in input().strip().split()]
        graph.append(tmp)
    # print(graph)
    max_v = 10**9
    dp = [[max_v]*n for i in range(n)]
    # init
    dp[0][0] = 0
    x, y = 0, 0
    s = 0
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    while x != n-1 and y != n-1:
        nxt_x = x
        nxt_y = y
        for i in range(4):
            nxt_x = x + dx[i]
            nxt_y = y + dy[i]
            if nxt_x < 0 or nxt_y < 0 or nxt_x >= n or nxt_y >= n:
                continue
            dp[nxt_x][nxt_y] = min(
                dp[nxt_x][nxt_y], dp[x][y] + abs(graph[nxt_x][nxt_y]-graph[x][y]))
            if dp[nxt_x][nxt_y] != max_v and nxt_x != x and nxt_y != y:
                x = nxt_x
                y = nxt_y
    print(dp[-1][-1])
    return

    # for i in range(1, n):
    #     s = abs(graph[0][i] - graph[0][i-1])
    #     dp[0][i] += s
    # for i in range(1, n):
    #     s = abs(graph[i][0] - graph[i-1][0])
    #     dp[i][0] += s

    # for i in range(1, n):
    #     for j in range(1, n):
    #         dp[i][j] = min(dp[i-1][j]+abs(graph[i][j] - graph[i-1][j]),
    #                        dp[i][j-1]+abs(graph[i][j]-graph[i][j-1]))
    # print(dp[-1][-1])


run()
