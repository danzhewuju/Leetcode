def run():
    n = int(input())
    will= [[0]*(n+1)]
    for i in range(n):
        tmp = [0]+[int(x) for x in input().strip().split()]
        will.append(tmp)
    place = [0]*(n+1)
    arrange = {}
    for i in range(1, n+1):
        for j in range(1, n+1):
            if will[i][j] not in arrange.keys():
                place[i] = will[i][j]
                arrange[will[i][j]] = i
                break
    print(' '.join([str(x) for x in place[1:]]))
    return 


run()
    
