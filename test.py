mod = 10**9 + 7
def multi(x, n):
    res = 1 
    while n > 0:
        if n % 2 == 1 : res = (res * x)%mod
        res = res * res % mod
        n //= 2
    return res

print(multi(2, 10))