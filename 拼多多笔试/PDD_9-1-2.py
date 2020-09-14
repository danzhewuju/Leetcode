def run():
    N, M = [int(x) for x in input().split()]
    matrix = []
    for _ in range(N):
        tmp = [int(x) for x in input().split()]
        matrix.append(tmp)
    blanks = []
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 0:
                blanks.append((i, j))
    if len(blanks) <= 1 or len(blanks) >= N*M-1:
        print(N*M-len(blanks))
        return 
    else:
        total = N * M - len(blanks)
        maxT = 1
        tmp = [[0]*M for _ in range(N)]
        for i in range(N):
            for j in range(M):
                tmp[i][j] = matrix[i][j]
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        while blanks:
            tmp = [[0]*M for _ in range(N)]
            for i in range(N):
                for j in range(M):
                    tmp[i][j] = matrix[i][j]
            curblank = blanks.pop(0)
            queue = []
            tmp[curblank[0]][curblank[1]] = 1
            queue.append(curblank)
            team = 0
            while queue:
                cur = queue.pop(0)
                x, y = cur[0], cur[1]
                tmp[x][y] = 0
                team += 1
                for i in range(4):
                    nxt_x, nxt_y = x + dx[i], y+dy[i]
                    if 0 <= nxt_x < N and 0 <= nxt_y < M and tmp[nxt_x][nxt_y] == 1:
                        queue.append((nxt_x, nxt_y))
            if team <= total:
                maxT = max(maxT, team)
            else:
                team -= 1
                maxT = max(maxT, team)
        print(maxT)
        return

run()
                
