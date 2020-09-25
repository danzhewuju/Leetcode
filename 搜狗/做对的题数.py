#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 返回一行字符串，表示原文。
# @param s1 string字符串一维数组 N*N的01矩阵，表示解密纸，0表示透明，1表示涂黑
# @param s2 string字符串一维数组 字符矩阵，表示密文
# @return string字符串
#
class Solution:
    def read(self):
        res = ""
        for i in range(len(self.key)):
            for j in range(len(self.key[0])):
                if self.key[i][j] == '0':
                    res += self.content[i][j]
        return res

    def trans_key(self):
        key = []
        for j in range(len(self.key[0])):
            tmp = []
            for i in range(len(self.key)-1, -1, -1):
                tmp.append(self.key[i][j])
            key.append(tmp)
        self.key = key
        return

    def rotatePassword(self, s1, s2):
        # write code here
        self.key = [list(x) for x in s1]
        self.content = [list(x) for x in s2]
        res = ""
        for _ in range(4):
            res += self.read()
            self.trans_key()
        print(res)
        return res

Sol = Solution()
Sol.rotatePassword(["1101","1010","1111","1110"],["ABCD","EFGH","IJKL","MNPQ"])
