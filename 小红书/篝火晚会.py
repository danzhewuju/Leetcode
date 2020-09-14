def run():
    n = int(input())
    memknow = [set()]
    A = [0]+[int(x) for x in input().split()]

    for i in range(1, n+1):
        tmp = set()
        tmp.add(i)
        memknow.append(tmp)

    cnt = 0
    flag = False
    while not flag:
        ithKnws = [set() for _ in range(n+1)]

        for i in range(1, n+1):
            if not flag:
                from_ = memknow[i]
                for j in from_:
                    if j == A[i]:
                        flag = True
                        break
                    ithKnws[A[i]].add(j)
        for i in range(1, n+1):
            if not flag:
                to_ = memknow[i]
                newknws = ithKnws[i]
                for j in newknws:
                    to_.add(j)
        cnt += 1
    print(cnt)
    return


run()
