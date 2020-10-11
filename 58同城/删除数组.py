#
# 删除重复元素
# @param array int整型一维数组 
# @return int整型一维数组
#
import collections 
class Solution:
    def removeDuplicate(self , array ):
        # write code here
        bit_map = set()
        n = len(array)
        for i in range(n-1, -1, -1):
            t = array[i]
            if t in bit_map:
                del array[i]
            else:
                bit_map.add(t)
        return array

Sol = Solution().removeDuplicate([1,1,1,2,1])
print(Sol)
        