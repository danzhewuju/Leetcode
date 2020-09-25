#
# 
# @param n int整型 初始球数
# @return double浮点型
#
# import random
# class Solution:
#     def test_one(self, n, flag):
#         # 利用随机条件模拟
#         if n <= 3: return 1-flag
#         while n > 0:
#             flag = 1 - flag
#             if n <= 3:
#                 break
#             a = random.randint(1, 4) # 随机减少
#             b = random.randint(0, 2)
#             n -= (a+b)
#         return flag # 最后返回谁赢

#     def calcProb(self , n ):
#         # write code here
#         K = 100000 # 进行10000次试验
#         res = 0
#         for i in range(K):
#             res += self.test_one(n, 0)
#         return res / K

import random
class Solution:
    def calcProb(self , n ):
        ans = 1.0
        m = 3
        if 0 < n < 4:
            return ans
        flag = True
        while n >= m+1:
            if n % (m+1) !=0 and flag:
                ans *= 0.5
                flag = False
                n -= n%(m+1)
            elif n%(m+1) == 0 and flag:
                ans *= 0.5
                flag = False
                n -= m
                n -= 1
            elif n%(m+1) !=0 and not flag:
                ans *= 0.5
                flag = True
                n -= n%(m+1)
                n -= 1
            else:
                ans *= 0.5
                n -= m
                flag = True
                n -= 1
        if n >0 and not flag:
            return 0.0
        ans = round(ans, 4)
        return ans


Sol = Solution()
print(Sol.calcProb(4))
