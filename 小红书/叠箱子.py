def run():
    T = int(input())
    res = 0
    info = []
    for i in range(T):
        tmp = [int(x) for x in input().split()]
        tmp.sort()
        info.append(tmp)
    data = sorted(info, key=lambda x: x[0]*x[1])
    for _, _ , h in data:
        res += h
    print(res)
    return 

while True:
    try:
        run()
    except:
        break
