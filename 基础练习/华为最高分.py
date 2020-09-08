n, m = [int(x) for x in input().split()]
student = [-1]+[int(x) for x in input().split()]
ans = []
for i in range(m):
    data = input().split()
    tmp = [int(data[1]), int(data[2])]
    if data[0] == 'Q':
        tmp.sort()
        s, e = tmp[0], tmp[1]
        res = max(student[s:e+1])
        ans.append(res)
    elif data[0] == 'U':
        s, e = tmp[0], tmp[1]
        student[s] = e
for d in ans:
    print(d)