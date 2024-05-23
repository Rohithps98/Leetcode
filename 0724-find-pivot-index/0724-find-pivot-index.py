class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pre = 0
        su = sum(nums)
        for i in range(len(nums)):
            if (pre*2)!=su-nums[i]:
                pre+=nums[i]
            else:
                return i
        return -1