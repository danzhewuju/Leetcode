# 利用并查集
class DIJ:
    def __init__(self, parent):
        self.parent = parent

    def find_root(self, x):
        root_x = x
        while self.parent[root_x] != -1:
            root_x = self.parent[root_x]
        return root_x  # 返回父亲节点

    def unit(self, x, y):
        root_x = self.find_root(x)
        root_y = self.find_root(y)
        if root_x != root_y:  # 表明父亲节点是一个人
            self.parent[root_x] = root_y  # 将父亲节点合并在一起
        return


def run():
    n, m, k = map(int, input().split())
    graph = []
    node = [-1]*(n+1)
    for i in range(m):
        a, b, c = map(int, input().split())
        if c <= k:
            graph.append((a, b))
    dij = DIJ(node)
    if len(graph) < n-1:
        print('No')
        return 
    for x, y in graph:
        dij.unit(x, y)  # 合并
    res = set()
    for t in range(1, n+1):
        root = dij.find_root(t)
        res.add(root)
        if len(res) > 1:
            print("No")
            return
    print("Yes")
    return


T = int(input())
for _ in range(T):
    run()
