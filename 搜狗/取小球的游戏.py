class Solution:
    def calcProb(self, n):
        # write code here
        self.d = [-1] * (n + 1)
        def helper(n):
            if self.d[n] != -1:
                return self.d[n]
            if n <= 3:
                self.d[n] = 1
            elif n == 4:
                self.d[n] = 0.5
            elif n > 4:
                case1 = helper(n - 1)/2.0+helper(n-2)/2.0
                case2 = helper(n - 2)/2.0+helper(n-3)/2.0
                case3 = helper(n - 3)/2.0+helper(n-4)/2.0
                self.d[n] = 1 - min(case1, case2, case3)
            return self.d[n]
        helper(n)