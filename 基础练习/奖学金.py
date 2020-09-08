def run():
    n, r, avg = [int(x) for x in input().split()]
    # n : 课程  r:满分   avg: 需要学习的平均分数
    a, b = [], []  # 平时分数， 分数的单价
    for i in range(n):
        x, y = [int(x) for x in input().split()]
        a.append(x)
        b.append(y)
    need_learned = avg*n-sum(a)   # 需要学习的分数
    # 先学习性价比高的课程
    info = dict(zip(range(n), b))
    info = sorted(info.items(), key=lambda x: x[1])

    res, p = 0, 0 # 最少的学习时间
    while need_learned > 0:
        index = info[p][0]
        price = info[p][1]
        p += 1
        d = r - a[index] # 最多的可以学习的分数
        if d <= need_learned:
            cost = d * price # 花费的时间
        else:
            cost = need_learned * price
        res += cost
        need_learned -= d
    return res

print(run())


