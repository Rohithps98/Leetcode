class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex <0:
            return []
        dp = [[1]*i for i in range(1,rowIndex+2)]
        for r in range(2,rowIndex+1):
            for c in range(1,r):
                dp[r][c] = dp[r-1][c-1]+dp[r-1][c]
        return dp[-1]