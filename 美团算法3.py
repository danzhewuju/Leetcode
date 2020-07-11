def input_():
    N = int(input())
    scores = []
    for i in range(N):
        nums = list(map(float, input().split()))
        scores.append(nums)
    return N, scores


if __name__ == '__main__':
    N, scores = input_()
    arrange = []
    ans = []
    maxScore = 0
    # 回溯
    def notValid(arrange, j):
        for a in arrange:
            if j == a[1]:
                return True
        return False

    def backtrack(col, maxS):
        if col == N:
            # print(arrange)
            s = 0
            for (i, j) in arrange:
                s += scores[i][j]
            if s > maxS:
                maxS = s
                tmp = []
                for (i,j) in arrange:
                    tmp.append((i,j))
                ans.append(tmp)

            return maxS
        for j in range(N):
            if notValid(arrange, j):  # 司机j已经被分配了订单
                continue
            arrange.append((col, j)) #将订单col分配给司机j
            maxS = max(maxS, backtrack(col + 1, maxS))
            arrange.pop() #撤销选择
        return maxS

    maxScore = backtrack(0, maxScore)
    print(maxScore)
    for (i, j) in ans[-1]:
        print((i+1, j+1))
