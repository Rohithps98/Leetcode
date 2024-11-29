class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows<=0:
            return []
        dp = [[1]*i for i in range(1,numRows+1)]
        for r in range(2, numRows):
            for c in range(1,r):
                dp[r][c] = dp[r-1][c-1]+dp[r-1][c]
        return dp