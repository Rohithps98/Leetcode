from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        a = []
        for i,j in c.items():
            if j>=2:
                a.append(i)
        return a