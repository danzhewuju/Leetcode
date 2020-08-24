'''
图的构建:
6
9
1 2 7
1 6 14
1 3 9
3 6 2
2 3 10
2 4 15
3 4 11
5 6 9
4 5 6



'''
def create_graph():
    print("节点的个数:",end='')
    n = int(input())
    print("边的个数:", end='')
    e = int(input())
    graph = [[0]*n for _ in range(n)]
    for i in range(e):
        s,e,v = [int(x) for x in input().split()]
        graph[s-1][e-1] , graph[e-1][s-1]= v, v
    return graph

def Dijkstra():
    graph = create_graph()
    n = len(graph)   # 节点的个数
    print(graph)
    vis = [0]*n  # 访问控制
    start, end = 0, 4 # 设置起点和终点
    max_distant = 10**9
    dis = [max_distant]*n  # 设置距离
    dis[start] = 0 # 初始化
    queue = [start]  # 设置队列
    while queue:
        node = queue.pop(0)
        vis[node] = 1
        for j,val in enumerate(graph[node]):
            if val != 0 and vis[j] == 0:
                queue.append(j) # 加入新的节点
                dis[j] = min(dis[j], dis[node]+val) # 更新节点的信息
    res = dis[end]
    print(dis)
    print(res)
    return res

Dijkstra()


        

