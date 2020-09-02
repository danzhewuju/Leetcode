import math
import time
def isPrime(n):
    tmp = int(math.sqrt(n))+1
    for i in range(2, tmp):
        if n % i == 0:
            return False
    return True

def method_1(n):
    res = []
    for i in range(2, n):
        if isPrime(i):
            res.append(i)
    return res

def method_2(n):
    dp = [True]*(n+1)
    dp[0], dp[1] = False, False
    for i in range(2, n+1):
        if dp[i]:
            j = 2
            while j*i < n+1:
                dp[i*j] = False
                j += 1
    res = [i for i, x in enumerate(dp) if x ]
    return res 

s = time.time()
res = method_1(10000000)
# print(res)
e = time.time()
print("Running time:{:.5f}".format(e-s))

s = time.time()
res = method_2(10000000)
# print(res)
e = time.time()
print("Running time:{:.5f}".format(e-s))
