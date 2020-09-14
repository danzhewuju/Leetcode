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
        graph[s-1][e-1] =  v
    return graph

def Dijkstra():
    graph = create_graph()
    n = len(graph)   # 节点的个数
    print(graph)
    start, end = map(int, input().split()) # 设置起点和终点
    start -= 1
    end -= 1
    # 初始化
    dis = [float('inf')]*n  # 距离
    vis = set()
    dis[start] = 0 # 初始化
    min_point = start
    while len(vis) < n : # 存在没有访问的节点
        vis.add(min_point)  # 将节点加入到访问的节点中
        for j,val in enumerate(graph[min_point]):
            if j not in vis and val > 0:
                dis[j] = min(dis[j], dis[min_point]+val)
        min_dist = float('inf')
        for i, d in enumerate(dis): # 找到没有访问过的最小的边
            if i not in vis and d > 0 and d < min_dist:
                min_dist = d
                min_point = i 
    res = dis[end]
    print(dis)
    print(res)
    return res

Dijkstra()


        

