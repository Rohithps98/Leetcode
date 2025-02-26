class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxsum = 0
        cursum = nums[0]
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                cursum += nums[i]
            else:
                maxsum = max(maxsum,cursum)
                cursum = nums[i]
        return max(maxsum,cursum)