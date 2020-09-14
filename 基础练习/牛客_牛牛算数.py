#
# 返回一个数字表示输出计算n个数字和的最小花费的时间。
# @param n int整型 表示有n个数。
# @param c int整型 参数c
# @param a int整型一维数组 ai表示第i个数的大小
# @return long长整型
#
import heapq
class Solution:
    def solve(self , n , c , a ):
        # write code here
        heapq.heapify(a) # 转化为小顶堆
        sum_ = 0
        while len(a) > 1:
            a_1 = heapq.heappop(a)
            a_2 = heapq.heappop(a)
            b = a_1 + a_2
            sum_ += b
            heapq.heappush(a, b)
        return c*sum_

Sol = Solution()
print(Sol.solve(5,76,[81,30,76,24,84]))


