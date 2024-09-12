class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # totalsum = sum(nums)
        # if totalsum%2:
        #     return False
        # target = totalsum//2
        # dp = [False]*(target+1)
        # dp[0] = True
        # for i in nums:
        #     for j in range(target,i-1,-1):
        #         dp[j] = dp[j] or dp[j-i]
        # return dp[target]
        if len(nums) == 1:
            return False
        if sum(nums) % 2 == 1:
            return False

        n = sum(nums) // 2

        dp = 1

        for num in nums:
            dp |= dp << num
        
        return dp & (1 << n)