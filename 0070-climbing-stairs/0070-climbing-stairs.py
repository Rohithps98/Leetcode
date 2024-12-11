class Solution:
    def climbStairs(self, n: int) -> int:
        # one = 2
        # two = 1
        # if n==1 or n==2:
        #     return n
        # for i in range(3,n+1):
        #     cur = one+two
        #     two = one
        #     one = cur
        # return one
        if n==1 or n==2:
            return n
        dp = [0]*n
        dp[0],dp[1] = 1,2
        for i in range(2,n):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[-1]