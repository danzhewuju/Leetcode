def clear(Q): # 清除Q为1 的情况
    m, n = len(Q), len(Q[0])
    for i in range(m-1, -1, -1):
        count = 0
        for j in range(n):
            count += Q[i][j]
        if count == n or count == 0:
            # 需要删除矩阵的所在行数
            Q = [[0]*n]+Q[:i]+Q[i+1:]
    return Q

# Q = [[1,1,1],[1, 0, 1],[0,0,0]]
# Q = clear(Q)
# print(Q)

def run():
    # 求最最大的最小
    frame = [int(x) for x in list(input())]
    brick = [int(x) for x in list(input())]
    m, n = max(frame)+ max(brick), len(frame)
    Q = [[0]*n for x in range(m)]
    for j, d in enumerate(frame): # 初始化 frame
        for i in range(m-1, m-1-d, -1):
            Q[i][j] = 1
    Q = clear(Q) # 本身进行构造
    res = float('inf')
    

    
    
        


