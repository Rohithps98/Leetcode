from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a = Counter(nums)
        for i,j in a.items():
            if j>len(nums)/2:
                return i