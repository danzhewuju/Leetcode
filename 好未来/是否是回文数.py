#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 是否为回文数
# @param num int整型 
# @return bool布尔型
#
class Solution:
    def isPalindrome(self , num ):
        # write code here
        res = []
        if num < 0:
            return False
        while num:
            t = num % 10
            res.append(t)
            num //= 10
        return True if res == res[::-1] else False

Sol = Solution()
print(Sol.isPalindrome(12321))

        