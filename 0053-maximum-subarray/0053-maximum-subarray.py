class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ms = nums[0]
        cs = 0
        for i in nums:
            cs = max(i,cs+i)
            ms = max(cs,ms)
        return ms