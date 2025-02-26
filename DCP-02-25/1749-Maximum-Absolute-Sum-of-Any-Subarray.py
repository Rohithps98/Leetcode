class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        maxsum,minsum,curmax,curmin = 0,0,0,0
        for i in nums:
            curmax = max(i,curmax+i)
            curmin = min(i,curmin+i)
            maxsum = max(maxsum,curmax)
            minsum = min(minsum,curmin)
        return max(abs(maxsum),abs(minsum))