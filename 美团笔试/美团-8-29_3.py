def run():
    n, x, y = [int(_) for _ in input().split()]
    graph = [[0]*(n+1) for _ in range(n+1)]
    for _ in range(n-1):
        p1, p2 = [int(_) for _ in input().split()]
        graph[p1][p2] = 1
        graph[p2][p1] = 1
    res = 0
    d, m_d = -10000000, 100000000
    def dfs(graph, x, y, count):
        nonlocal d, m_d
        if y == x:
            m_d = min(m_d, count)
            return 
        if 1 not in graph[y]:
            d = max(d, count)
            return 
        p = graph[y]
        for i in range(len(p)):
            if p[i] == 1:
                graph[y][i] = 0
                graph[i][y] = 0
                dfs(graph, x, i, count + 1)
    dfs(graph, x, y, 0)
    # print(d, m_d)
    print(d+m_d)

if __name__ == "__main__":
    run()
    
