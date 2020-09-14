def run():
    N, M = [int(x) for x in input().split()]
    data = []
    for _ in range(M):
        x = int(input())
        if data:
            for y in data:
                if x % y == 0:
                    continue
        data.append(x)

    def isright(x):
        for d in data:
            if x % d == 0:
                return True
        return False

    res = 0
    for i in range(1, N+1):
        if isright(i):
            res += 1
    print(res)
    return res


run()
