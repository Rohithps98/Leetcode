class Solution:
    def divisorGame(self, n: int) -> bool:
        if n==1:
            return False
        if n==2:
            return True
        dp = [False]*(n+1)
        dp[1] = False
        dp[2] = True
        for i in range(3,n+1):
            for x in range(1,i):
                if (i%x)==0 and not dp[i-x]:
                    dp[i] = True
                    break
        return dp[n]