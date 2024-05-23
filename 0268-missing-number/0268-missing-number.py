class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        asu = (n*(n+1))//2
        cs = sum(nums)
        return asu-cs