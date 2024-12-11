class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # def dfs(i,j):
        #     if i>=len(grid) or j>=len(grid[0]):
        #         return float('inf')
        #     if i==len(grid)-1 and j==len(grid[0])-1:
        #         return grid[i][j]
        #     return grid[i][j]+min(dfs(i+1,j),dfs(i,j+1))
        # return dfs(0,0)
        m,n = len(grid),len(grid[0])
        dp = grid[0][:]
        for j in range(1,n):
            dp[j]+=dp[j-1]
        for i in range(1,m):
            dp[0]+=grid[i][0]
            for j in range(1,n):
                dp[j] = grid[i][j]+min(dp[j],dp[j-1])
        return dp[-1]