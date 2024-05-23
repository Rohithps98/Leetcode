class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # n = len(nums)
        # asu = (n*(n+1))//2
        # cs = sum(nums)
        # return asu-cs
        # miss = len(nums)
        # for i,num in enumerate(nums):
        #     miss ^= i^num
        # return miss
        a = set(nums)
        n = len(nums)
        for i in range(n+1):
            if i not in a:
                return i