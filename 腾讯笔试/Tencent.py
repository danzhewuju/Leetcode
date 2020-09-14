import math
def run():
    T = int(input())
    ans = []
    for i in range(T):
        res = 0
        A, B, C, D = [int(x) for x in input().split()]
        x = C
        dx = 1e-7
        res = (A*(math.pow(D, 3)- math.pow(C, 3)))/3+(D**2-C**2)/2 + B*(D-C)
        res = round(res, 6)
        ans.append(res)
    return ans

res = run()
for idx, d in enumerate(res):
    if idx == len(res) -1:
        print(d, end='')
    else:
        print(d)