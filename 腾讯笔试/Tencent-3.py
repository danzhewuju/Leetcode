'''
1. 快速幂乘法思想，如果是奇数就乘当前的数，如果是偶数，就直接乘法
'''
n = int(input())
mod = 10 ** 9 + 7
def cal(x, n, p):
    res = 1
    while n > 0:
        if n % 2:
            res = res * x % p
        x = x * x % p
        n = n//2
    return res
 
ans = n * cal(2, n - 1, mod)
ans = ans % mod
print(ans)