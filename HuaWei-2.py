import collections
import math
def getC_n_m(n, m): # n个节点m课树的个数
    sum_ = int(math.pow(2, n))
    b = 1
    a = 1
    for i in range(m, 1, -1):
        a *= i
    for i in range(m):
        b *= (sum_-i)
    res = int(b/a)
    return res%1000000007
def run():
    N = int(input())
    data = [int(x) for x in input().split()]
    data_dict = dict(collections.Counter(data))
    count = 1
    res = 1
    max_deep = len(data_dict)
    for i in range(1, max_deep):
        n = data_dict[i-1]
        m = data_dict[i]
        res *= getC_n_m(n, m)
        res = res % (1000000007)
    return res % (1000000007)

print(run())



