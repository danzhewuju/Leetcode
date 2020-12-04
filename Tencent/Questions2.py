def run():
    T = int(input())
    res = []
    for i in range(T):
        n, k = map(int, input().split())
        nums = [int(x) for x in input().split()]
        if k == 0:
            res.append(0)
            continue
        nums.sort()
        nums = nums[:2*k]
        sum_ = 0
        for t in range(k):
            sum_ += nums.pop(0)*nums.pop()
        res.append(sum_)
    return res

res = run()
for d in res:
    print(d)


        
