def run():
    def dfs(i, j, graph, direct, cost):
        nonlocal res
        if i == x and j == y:
            res = min(res, cost)
            return
        graph[i][j] = 'x'
        for dx, dy, c in direct:
            new_x, new_y = i+dx, j+dy
            if 0 <= new_x < n and 0 <= new_y < m and graph[new_x][new_y] == 'o':
                dfs(new_x, new_y, graph, direct, cost + c)
        graph[i][j] = 'o'
        return

    T = int(input())
    for _ in range(T):
        n, m = map(int, input().split())
        x, y = map(int, input().split())
        a, b, c, d = map(int, input().split())
        direct = [(-1, 0, a), (1, 0, b), (0, -1, c), (0, 1, d)]
        graph = []
        for _ in range(n):
            tmp = list(input())
            graph.append(tmp)
        res = float('inf')

        if graph[x][y] == 'x':
            print(-1)
            return
        dfs(0, 0, graph, direct, 0)
        if res != float('inf'):
            print(res)
        else:
            print('-1')
        return


run()
