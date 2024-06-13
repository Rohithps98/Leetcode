from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        a = Counter(nums)
        for i,j in a.items():
            if j>len(nums)/3:
                res.append(i)
        return res