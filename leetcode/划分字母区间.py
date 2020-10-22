# 字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，
# 同一个字母只会出现在其中的一个片段。返回一个表示每个字符串片段的长度的列表。

class Solution:
    def partitionLabels(self, S):
        # 区间的合并
        stack = []
        last = [-1]* 26
        # 记录终点的位置
        for i, c in enumerate(S):
            last[ord(c)-ord('a')] = i
        start, end = 0, 0
        for i, c in enumerate(S):
            index = ord(c) -ord('a')
            p = last[index]
            end = max(end, p)
            if end > i:
                continue
            else:
                stack.append(end-start+1)
                start = end + 1
        return stack

print(Solution().partitionLabels('ababcbacadefegdehijhklij'))