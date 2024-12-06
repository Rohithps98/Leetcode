class Solution:
    def countBits(self, n: int) -> List[int]:
        # res = []
        # for i in range(n+1):
        #     a = bin(i)[2:].count('1')
        #     res.append(a)
        # return res
        dp = [0]*(n+1)
        for i in range(1,n+1):
            dp[i] = dp[i>>1]+(i&1)
        return dp