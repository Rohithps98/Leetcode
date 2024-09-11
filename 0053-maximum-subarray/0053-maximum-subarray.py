class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # ms = nums[0]
        # cs = 0
        # for i in nums:
        #     cs = max(i,cs+i)
        #     ms = max(cs,ms)
        # return ms
        n = len(nums)
        dp = [0]*n
        dp[0] = nums[0]
        for i in range(1,n):
            dp[i] = max(nums[i],dp[i-1]+nums[i])
        return max(dp)