
'''
测试用例:
 

'''
n, m, k = [int(x) for x in input().split()]
graph ={}
# 构建图
val = {}
for i in range(m):
    x, y ,_= [int(x) for x in input().split()]
    if x not in graph:
        graph[x] = [y]
    else:
        graph[x] += [y]
    if y not in graph:
        graph[y] = [x]
    else:
        graph[y] += [x]
    val[(x, y)] = 1
    val[(y, x)] = 1

for i in range(k):
    x, y = [int(x) for x in input().split()]
    if x not in graph:
        graph[x] = [y]
    else:
        if y not in graph[x]:
            graph[x] += [y]
    val[(x, y)] = 0
vis = [0]*(n+1)
vis[0], vis[1] = 1, 1
def run():
    def dfs(node, sum_):
        nonlocal res
        if node == n:  # 表示必定可以达到
            res = min(res, sum_)
            return 
        for y in graph[node]:
            if vis[y] == 0:
                vis[y] = 1
                dfs(y, sum_+val[(node, y)])
    res = float('inf')
    dfs(1, 0)
    if res == float('inf'): res = -1
    print(res)
run()