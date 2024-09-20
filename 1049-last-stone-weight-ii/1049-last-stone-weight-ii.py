class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        totalsum = sum(stones)
        target = totalsum//2
        dp = [False]*(target+1)
        dp[0] = True
        for stone in stones:
            for i in range(target,stone-1,-1):
                dp[i] = dp[i] or dp[i-stone]
        for s in range(target,-1,-1):
            if dp[s]:
                return totalsum-2*s