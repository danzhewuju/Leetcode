'''
给你一个数组 arr ，该数组表示一个从 1 到 n 的数字排列。有一个长度为 n 的二进制字符串，该字符串上的所有位最初都设置为 0 。

在从 1 到 n 的每个步骤 i 中（假设二进制字符串和 arr 都是从 1 开始索引的情况下），二进制字符串上位于位置 arr[i] 的位将会设为 1 。

给你一个整数 m ，请你找出二进制字符串上存在长度为 m 的一组 1 的最后步骤。一组 1 是一个连续的、由 1 组成的子串，且左右两边不再有可以延伸的 1 。

返回存在长度 恰好 为 m 的 一组 1  的最后步骤。如果不存在这样的步骤，请返回 -1 。

'''
class Solution:
    import bisect
    def findLatestStep(self, arr: List[int], m: int) -> int:
        if m == len(arr):
            return m
        l = [0, len(arr)+1]
        for idx, p in enumerate(arr[::-1]):
            i = bisect.bisect(l, p)
            l.insert(i, p)
            # print(l)
            if l[i+1]-l[i] -1 == m or l[i] - l[i-1] -1 == m:
                return len(arr) - idx-1
        return -1

