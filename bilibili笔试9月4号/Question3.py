class Solution:
    def print_diamond(self, n):
        if n % 2 == 0: return ""
        matrix= [['*']*n for _ in range(n)] # 初始化一个二维数组
        # 寻找对称情况
        mid = n // 2
        # cut_str = [['*']*(mid+1) for _ in range(mid)] # 左上角，包含轴线
        # 只考虑左上角
        for j in range(mid + 1): # 最下轴的情况
            matrix[mid][j] = str(j+1)
        for i in range(mid+1):  # 最右的情况
            matrix[i][mid] = str(i+1)
        
        for i in range(mid): # 开始考虑到一般情况
            for j in range(mid, mid-i-1, -1): # 逆序
                t = i+1 - mid + j # 需要填充的值 
                matrix[i][j] = str(t)
        #开始进行左右的翻转
        for i in range(mid+1):
            for j in range(mid+1, n):
                matrix[i][j] = matrix[i][n-1-j]
        
        # 上下翻转
        for i in range(mid+1, n):
            for j in range(n):
                matrix[i][j] = matrix[n-1-i][j]
        
        res = ["".join(x) for x in matrix]
        ans = "|".join(res)
        return ans


Sol = Solution()
print(Sol.print_diamond(5))

