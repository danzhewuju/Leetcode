# 需要进行图的构建
import collections


def updategraph(graph, new_node):  # 图更新策略相邻的节点必定构成图
    if new_node in graph.keys():
        return graph
    x, y = new_node[0], new_node[1]
    direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 方向坐标
    for dx, dy in direct:
        new_x, new_y = x + dx, y + dy
        if (new_x, new_y) in graph.keys():
            # 构建双边
            graph[new_node] += [(new_x, new_y)]
            graph[(new_x, new_y)] += [new_node]
    return graph


def run():
    T = int(input())
    direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 方向坐标
    for i in range(T):
        N = int(input())
        # 需要构建邻接表
        graph = collections.defaultdict(list)  # 邻接表
        graph[(0, 0)] = []

        x, y = 0, 0  # 将初始坐标设置为(0,0)
        target = (0, 0)  # 标记结果以及最终目的地
        for i in range(N):  # 图构建不够完整
            op, r = map(int, input().split())
            if r == 1:  # 操作合法
                dx, dy = direct[op]
                new_x, new_y = x + dx, y + dy
                # graph[(x, y)] += [(new_x, new_y)] # 构建一个边
                # graph[(new_x, new_y)] += [(x, y)] # 双向边
                graph = updategraph(graph, (new_x, new_y))
                x, y = new_x, new_y  # 更新坐标
                if i == N-1:
                    target = (x, y)
        res = float('inf')
        vis = {x: 0 for x in graph.keys()}  # 表示的是访问位

        def dfs(node, distance):
            nonlocal res
            # if vis[node] == 1:
            #     return
            if node == target:
                res = min(res, distance)
                return
            if distance >= res:
                return 
            vis[node] = 1
            for next_node in graph[node]:
                if vis[next_node] == 0:
                    dfs(next_node, distance+1)
            return
        dfs((0, 0), 0)
        print(res)
    return


run()
