class Interval:
     def __init__(self, a=0, b=0):
        self.start = a
        self.end = b

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 返回Interval类，start代表汪仔最少做对了多少道题，end代表汪仔最多做对了多少道题。
# @param n int整型 选择题总数
# @param k int整型 朋友做对的题数
# @param str1 string字符串 长度为n只包含ABCD的字符串，其中第i个代表汪仔第i题做出的选择
# @param str2 string字符串 长度为n只包含ABCD的字符串，其中第i个代表朋友第i题做出的选择
# @return Interval类
#
class Solution:
    def solve(self , n , k , str1 , str2 ):
        c = 0 # 完全相同的个数
        for i in range(n):
            if str1[i] == str2[i]:
                c += 1
        if n-k >= c:
            r1 = 0
        else:
            r1 = c-n+k
        if c == 0:
            r2 = n-k
        elif k <=c:
            r2 = n -c +k
        else:
            r2 = n -k +c
        res = Interval(r1, r2)
        return res