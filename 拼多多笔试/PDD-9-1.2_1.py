def cal_max_count(graph):
    # 计算图的最大联通分量
    res = 0
    N, M = len(graph), len(graph[0])
    direct = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    loc = [(i, j) for i in range(N) for j in range(M) if graph[i][j] == 1]
    

def run():
    N, M = [int(x) for x in input().split()]
    matrix = []
    for _ in range(N):
        tmp = [int(x) for x in input().split()]
        matrix.append(tmp)
    