def run():
    n = int(input())
    graph = []  # 需要构建一个图
    for _ in range(n):
        tmp = list(input())
        graph.append(tmp)
    if n <= 2:
        return graph  # 不需要进行处理
    # 矩阵的范围，0 必须在 [1,n-1) 的范围内才有有效
    print(graph)
    direct = [(1, 0), (0, 1), (0, -1), (-1, 0)]

    def dfs(i, j):  # 构建深度搜索，搜索的过程中不能出现连通点出现在边界上, 坐标i,j 连通点位0的所有坐标保存在info里面
        if i != 0 and i != n-1 and j != 0 and j != n-1:
            info['path'].append((i, j))
            vis[i][j] = 1
            for dx, dy in direct:
                new_x, new_y = i + dx, j+dy
                if graph[new_x][new_y] == '0' and vis[new_x][new_y] == 0:
                    dfs(new_x, new_y)
            vis[i][j] = 0
        else:  # 出现在了边界的情况，此时所有的节点不能被染色另外的保存
            info['flag'] = False  # 表明节点存在气
            return

    res = []
    non_vist = set()  # 无需访问的节点, 里面保存的是坐标
    for i in range(1, n-1):
        for j in range(1, n-1):
            if (i, j) not in non_vist and graph[i][j] == '0':
                info = {'flag': True, 'path': []}  # 全局变量
                vis = [[0]*n for _ in range(n)]
                dfs(i, j)
                if info['flag']:
                    for x, y in info['path']:
                        graph[x][y] = '1'
                        # print(x, y)
                else:
                    for x, y in info['path']:
                        non_vist.add((x, y))
    return graph


graph = run()
res = ["".join(graph[i]) for i in range(len(graph))]
for d in res:
    print(d)
