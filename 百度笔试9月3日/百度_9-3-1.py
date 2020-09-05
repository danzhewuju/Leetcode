def run():
    n, m, k = map(int, input().strip().split()) # 个数， 重量， 钱数
    cost = []
    for i in range(n):
        tmp = [int(x) for x in input().strip().split()]
        cost.append(tmp)
    cost = sorted(cost, key=lambda x: (-x[2], x[0], x[1]))
    print(cost)
    res = 0
    for p, w, v in cost:
        if m >= w and k >= p:
            m -= w
            k -= p
            res += 1
    print(res)
    return 

run()