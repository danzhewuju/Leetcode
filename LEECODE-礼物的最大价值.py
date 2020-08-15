class Solution:
    def maxValue(self, grid):
        res = 0
        m, n = len(grid), len(grid[0])
        # # 1.利用深度优先搜索(超时)
        # def dfs(loc, sum_):
        #     nonlocal  res
        #     if loc == (m-1, n-1):
        #         res = max(res, sum_)
        #     for dx, dy in [(1, 0), (0, 1)]:
        #         x, y = loc[0]+dx, loc[1]+dy
        #         if 0<= x < m and 0<= y < n:
        #             dfs((x, y), sum_+grid[x][y])
        # dfs((0, 0), grid[0][0])

        dp =[[0]*n for _ in range(m)]  # dp[i][j] 表示到达（i,j）时获得的最大的价值
        last = 0
        for j in range(n):
            last += grid[0][j]
            dp[0][j] = last
        last = 0
        for i in range(m):
            last += grid[i][0]
            dp[i][0] = last
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])+grid[i][j]
        return dp[-1][-1]

a = [[7,1,3,5,8,9,9,2,1,9,0,8,3,1,6,6,9,5],[9,5,9,4,0,4,8,8,9,5,7,3,6,6,6,9,1,6],[8,2,9,1,3,1,9,7,2,5,3,1,2,4,8,2,8,8],[6,7,9,8,4,8,3,0,4,0,9,6,6,0,0,5,1,4],[7,1,3,1,8,8,3,1,2,1,5,0,2,1,9,1,1,4],[9,5,4,3,5,6,1,3,6,4,9,7,0,8,0,3,9,9],[1,4,2,5,8,7,7,0,0,7,1,2,1,2,7,7,7,4],[3,9,7,9,5,8,9,5,6,9,8,8,0,1,4,2,8,2],[1,5,2,2,2,5,6,3,9,3,1,7,9,6,8,6,8,3],[5,7,8,3,8,8,3,9,9,8,1,9,2,5,4,7,7,7],[2,3,2,4,8,5,1,7,2,9,5,2,4,2,9,2,8,7],[0,1,6,1,1,0,0,6,5,4,3,4,3,7,9,6,1,9]]
S = Solution()
print(S.maxValue(a))


