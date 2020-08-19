    
def run():
    flag = 17
    M, N = [int(x) for x in input().split()]
    # M, N = 10, 10
    if M <= 0 or N <= 0:
        return []
    count = 1
    direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    res = [] # 保存的结果
    x, y = 0, 0 # 坐标位置
    p = 0 # 指向的方向
    bit_map = [[0]*N for _ in range(M)]
    bit_map[0][0] = 1

    while count < M*N:
        dx, dy = direct[p%4]
        while 0 <=x+dx<M and 0<=y+dy<N and bit_map[x+dx][y+dy] == 0 :
            count += 1
            x, y = x+dx, y+dy
            bit_map[x][y] = 1
            if count == flag:
                res.append([x,y])
                flag += 20
        p = (p+1)%4
    return res

res = run()
if res == []:
    print('[]')
else:
    for i in range(len(res)):
        if i == 0:
            print('[[{},{}],'.format(res[i][0], res[i][1]), end='')
        if i == len(res) - 1:
            print('[{},{}]]'.format(res[i][0], res[i][1]), end='')
        if 0<i<len(res)-1:
            print('[{},{}],'.format(res[i][0], res[i][1]), end='')