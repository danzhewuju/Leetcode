class Solution:
    def judgePoint24(self, nums):
        # 利用深度优先搜索的方法来进行回溯
        res = False
        op = ['+', '-', '*', '/']
        def helper(new_nums):
            nonlocal res
            if len(new_nums) == 2:
                for p in op:
                    tmp = 0
                    if p == '+' : 
                        tmp = new_nums[0] + new_nums[1] 
                        if abs(tmp-24) < 1e-9:
                            res = True
                    if p == '-' : 
                        tmp = new_nums[0] - new_nums[1] 
                        if abs(tmp-24) < 1e-9:
                            res = True
                        tmp = new_nums[1] - new_nums[0] 
                        if abs(tmp-24) < 1e-9:
                            res = True
                    if p == '*' : 
                        tmp = new_nums[0] * new_nums[1] 
                        if abs(tmp-24) < 1e-9:
                            res = True
                    if p == '/'  and new_nums[1] != 0: 
                        if new_nums[1] != 0:
                            tmp = new_nums[0] / new_nums[1] 
                            if abs(tmp-24) < 1e-9:
                                res = True
                        if new_nums[0] != 0:
                            tmp = new_nums[1] / new_nums[0] 
                            if abs(tmp-24) < 1e-9:
                                res = True
                return 
            for i in range(len(new_nums)):
                for j in range(i+1, len(new_nums)):
                    a, b = new_nums[i], new_nums[j]
                    tmp = new_nums.copy()
                    tmp.remove(a)
                    tmp.remove(b)
                    helper(tmp+[a+b])
                    helper(tmp+[a-b])
                    helper(tmp+[b-a])
                    helper(tmp+[a*b])
                    if b != 0: helper(tmp+[a/b])
                    if a != 0: helper(tmp+[b/a])
        helper(nums)
        return res

Sol = Solution()
a = [3, 3, 8, 8]
print(Sol.judgePoint24(a))

            
