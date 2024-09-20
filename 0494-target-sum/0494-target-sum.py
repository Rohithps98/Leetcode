class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        totalsum = sum(nums)
        if totalsum<0 or (totalsum+target)%2:
            return 0
        required = (totalsum+target)//2
        if required<0:
            return 0
        dp = [0]*(required+1)
        dp[0] = 1
        for i in nums:
            for j in range(required,i-1,-1):
                dp[j]+=dp[j-i]
        return dp[required]
    