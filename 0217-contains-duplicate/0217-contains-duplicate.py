from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a = Counter(nums)
        for i,j in a.items():
            if j>1:
                return True
        return False
        # a = set()
        # for i in nums:
        #     if i in a:
        #         return True
        #     a.add(i)
        # return False