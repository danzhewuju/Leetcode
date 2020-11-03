#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 
# @param nums int整型一维数组 
# @return int整型
#
class Solution:
    def uniqueAward(self , nums ):
        # write code here
        d = nums[0]
        for t in nums[1:]:
            d = d^t
        return d

print(Solution().uniqueAward([3,2,2]))