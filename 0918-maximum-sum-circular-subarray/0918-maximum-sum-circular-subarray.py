class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def kadane(arr):
            cs=ms=arr[0]
            for i in arr[1:]:
                cs = max(i,cs+i)
                ms = max(cs,ms)
            return ms
        maxkadane = kadane(nums)
        totalsum = sum(nums)
        minsubarray = kadane([-x for x in nums])
        maxcircular = totalsum+minsubarray
        return max(maxcircular,maxkadane) if maxcircular!=0 else maxkadane