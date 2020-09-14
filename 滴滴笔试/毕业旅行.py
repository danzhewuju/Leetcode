def run():
    month_info = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    n, m = map(int, input().split())
    graph = [[0]*(n+1) for _ in range(n+1)]
    for i in range(m):
        u, v, t = map(int, input().split())
        graph[u][v], graph[v][u] = t, t  # 构建无向图
    info = input().split()
    s, e = int(info[0]), int(info[1])
    start = info[-1]  # 出发的时间
    # 最短路径算法
    vis = [0]*(n+1)
    dis = [float('inf')]*(n+1)
    queue = [s]  # 将起始时间加入栈中
    dis[s] = 0
    while queue:
        node = queue.pop(0)
        vis[node] = 1  # 访问控制
        for next_node, t in enumerate(graph[node]):
            if t != 0:  # 表示有路径
                dis[next_node] = min(dis[next_node], dis[node]+t)
                if vis[next_node] == 0:  # 入栈条件
                    queue.append(next_node)  # 入栈
    spend_time = dis[e]
    pre_str = start.split('/')[0]
    hour = int(start.split('/')[-1])
    month, day = int(pre_str.split('.')[0]), int(pre_str.split('.')[-1])

    hour += spend_time
    d_day = hour // 24
    hour = hour % 24  # 小时
    day += d_day
    month_day = month_info[month] # 当月的天数
    d_month = day // month_day
    day %= month_day
    month += d_month

    res = "{}.{}/{}".format(month, day, hour)
    print(res)
    return


run()
