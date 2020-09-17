def run():
    N, K1, K2 = map(int, input().split())
    X, Y, Z = map(int, input().split())
    money = X*17*29+Y*29+Z
    d = K1 - K2
    cost = []
    value = []
    for i in range(N):
        tmp = [int(x) for x in input().split()]
        t = tmp[0]*17*29 + tmp[1]*29 + tmp[2]
        cost.append(t)
        value.append(tmp[-1])
    if d < 0:
        print("Yes")
        print("{} {} {}".format(X, Y, Z))
        return
    else:
        avg_spend = [value[i]/cost[i] for i in range(N)]
        dict_info = {i: (avg_spend[i], cost[i]) for i in range(N)}
        data = sorted(dict_info.items(),
                      key = lambda x: (-x[1][0], x[1][1]))  # 根据花费多少排序
        i = 0
        stack = []
        while i < len(data):
            index = data[i][0]
            p = value[index]
            if money >= cost[index]:
                if p <= d:
                    d -= p
                    money -= cost[index]
                    # del(data[i])
                    # i -= 1
                else:
                    stack.append((money, index))  # 当时剩余的钱数，假设花费的项目编号
            i += 1
        money, index = -1, -1
        print(stack)
        for m, i in stack:
            c = cost[i]
            if m >= c:  # 还有余钱剩下
                if m - c > money:
                    money = m-c
                    index = i
        print(money)
        if money >= 0:
            X = money // (17 * 29)
            money %= 17 * 29
            Y = money // 29
            Z = money % 29
            print('Yes')
            print("{} {} {}".format(X, Y, Z))
        else:
            print('No')
    return


run()
