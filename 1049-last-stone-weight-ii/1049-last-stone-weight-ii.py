class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        totalsum = sum(stones)
        target = totalsum//2
        dp = [False]*(target+1)
        dp[0] = True
        for i in stones:
            for j in range(target,i-1,-1):
                dp[j] = dp[j] or dp[j-i]
        for s in range(target,-1,-1):
            if dp[s]:
                return totalsum-2*s