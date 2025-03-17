from collections import Counter
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        a = Counter(nums)
        if len(nums)%2 != 0:
            return False
        for k,v in a.items():
            if v==1 or v%2 != 0:
                return False
        return True