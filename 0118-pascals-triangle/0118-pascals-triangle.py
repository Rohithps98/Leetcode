class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows<=0:
            return []
        # dp = [[1]*(i+1) for i in range(numRows)]
        a = []
        for r in range(1,numRows+1):
            dp = [1]*r
            for c in range(1,r-1):
                dp[c] = a[r-2][c]+a[r-2][c-1]
            a.append(dp)
        return a