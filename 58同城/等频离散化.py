#
# 等频离散化
# @param A int整型一维数组 从小到大已排序整数数列A
# @param K int整型 划分段数
# @return int整型二维数组
#
class Solution:
    def discretize_by_frequency(self , A , K ):
        # write code here
        res = [[] for _ in range(K)]
        count = 0
        min_length = 0
        for d in A:
            min_length = min([len(x) for x in res])
            while True:
                i = count
                if not res[i]:
                    res[i].append(d)
                    break
                elif d == res[i][-1]:
                    res[i].append(d)
                    break
                elif len(res[i]) == min_length:
                    res[i].append(d)
                    break
                else:
                    count = (count+1)%K
        return res

print(Solution().discretize_by_frequency([1, 1, 1,  2,  2 , 4,  5, 5],3))



        