'''
找规律
l = int(sqrt(n))+1 // 
'''
import math
def run():
    T = int(input())
    a = [int(x) for x in input().split()]
    res = []
    max_matrix = 2500 # 设置最多的构成的矩形 
    dp = [0]*max_matrix
    dp[0], dp[1] = 0, 4 # 初始化
    for r in range(2, len(dp)):
        n = int(math.sqrt(r)) # 构成正方向的边长
        if n**2 == r:
            n -= 1
            index = 2*n + 1
        else:
            index = r- n**2 # t 表示多余的方块
        if 0 < index <= n:
            dp[r] = dp[n**2] + 3 +(index - 1 ) *2
        else:
            dp[r] = dp[n**2] + 6 + (index-2) *2
    # 可利用二分查找快速定位
    print(dp[:20])
    for d in a:
        l, r = 0, len(dp)-1
        while l <= r:
            mid = (l+r) // 2
            if dp[mid] <= d:
                l = mid + 1
            else:
                r = mid - 1
        if dp[l] > d:
            print(l-1)
        else:
            print(l) 
    return 
if __name__ == "__main__":
    run()
    pass