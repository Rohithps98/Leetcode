from collections import Counter
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        a = Counter(nums)
        c = 0
        for i,j in a.items():
            if j==1:
                c+=i
        return c