class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows<=0:
            return []
        dp = [[1]*(i+1) for i in range(numRows)]
        for row in range(2,numRows):
            for col in range(1,row):
                dp[row][col] = dp[row-1][col-1]+dp[row-1][col]
        return dp