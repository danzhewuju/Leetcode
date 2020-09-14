class Solution:
    def gcd(self, x, y):
        while y > 0:
            x, y = y, x % y
        return x 
    def calmaxcommonfactor(self, L):
        if not L: # 不存在
            return -1
        res = L[0]
        for d in L[1:]:
            res = self.gcd(res, d)
        return res


Sol = Solution()
print(Sol.calmaxcommonfactor([2, 4, 5]))

