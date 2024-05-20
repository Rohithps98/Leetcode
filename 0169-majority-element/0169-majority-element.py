class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a = {}
        for i in nums:
            a[i] = 1+a.get(i,0)
            if a[i]>len(nums)/2:
                return i