#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 寻找朋友总数
# @param M int整型二维数组 
# @return int整型
#
class Jdf:
    def __init__(self, parent):
        self.parent = parent
    
    def find_root(self, x):
        root_x = x
        while self.parent[root_x] != -1:
            root_x = self.parent[root_x]
        return root_x
    
    def unio(self, x, y):
        root_x = self.find_root(x)
        root_y = self.find_root(y)
        if root_x != root_y:
            self.parent[root_y] = root_x
        return 

class Solution:
    def findFriendNum(self , M ):
        # write code here
        N = len(M)
        if not M:
            return 0; 
        parent = [-1]*N
        jdf = Jdf(parent)
        for i in range(N):
            for j in range(i+1):
                if M[i][j] == 1:jdf.unio(i, j)
        relation = set()
        for t in range(N):
            m = jdf.find_root(t)
            relation.add(m)
        return len(relation)

M = [[1,0,0],[0,1,0],[0,0,1]]
print(Solution().findFriendNum(M))