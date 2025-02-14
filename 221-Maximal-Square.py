class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0 
        m,n = len(matrix),len(matrix[0])
        maxside = 0
        prev = 0
        dp = [0]*(n+1)
        for i in range(m):
            for j in range(n):
                temp = dp[j+1]
                if matrix[i][j]=='1':
                    dp[j+1] = min(dp[j+1],dp[j],prev)+1
                    maxside = max(maxside,dp[j+1])
                else:
                    dp[j+1] = 0
                prev = temp
        return maxside**2