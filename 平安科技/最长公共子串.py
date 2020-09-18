#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 
# @param s1 string字符串 
# @param s2 string字符串 
# @return int整型
#
class Solution:
    def find_lcsubstr(self , s1 , s2 ):
        # write code here
        if not s1 or not s2:
            return 0
        if len(s1) > len(s2):
            s1, s2 = s2, s1
        m = len(s1)
        res = 0
        for i in range(m):
            for j in range(i+1, m+1):
                if j - i > res and s1[i:j] in s2:
                    res = j-i
        return res

Sol = Solution()
print(Sol.find_lcsubstr("banana","bake")) 

