# 素数之和的个数
import math
def isPrime(d):
    sqr = int(math.sqrt(d)) +1
    count = 0
    for i in range(2, sqr):
        if d % i == 0:
            count += 1
        if count > 0:
            return False
    return True

n = int(input())
z =  list(filter(isPrime, range(2, n+1)))
res = 0
# 设置窗口大小 
w = 1
while w < len(z):
    start = 0
    while sum(z[start:start+w]) < n:
        start += 1
    if sum(z[start:start+w]) == n:
        res += 1
    w += 1
print(res)

