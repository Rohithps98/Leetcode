class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalsum = sum(nums)
        if totalsum%2:
            return False
        target = totalsum//2
        dp = [False]*(target+1)
        dp[0] = True
        for i in nums:
            for j in range(target,i-1,-1):
                dp[j] = dp[j] or dp[j-i]
        return dp[target]