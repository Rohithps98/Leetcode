class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        if grid[0][0]==1 or grid[m-1][n-1]==1:
            return 0
        dp = [0]*n
        dp[0]=1
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    dp[j]=0
                elif j>0:
                    dp[j]+=dp[j-1]
        return dp[-1]