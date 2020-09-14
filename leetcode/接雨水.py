'''
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        """双指针的解法"""
        p_1, res, key, p_2 = 0, 0, 0, len(height) - 1
        while p_2 > p_1:
            key = min(height[p_1], height[p_2])
            while height[p_1] <= key and p_2 > p_1:
                res += max(key-height[p_1], 0)
                p_1 += 1
            key = min(height[p_1], height[p_2])
            while height[p_2] <= key and p_2 > p_1:
                res += max(key-height[p_2], 0)
                p_2 -= 1
        return res

            



