class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def kadane(arr):
            cs = ms = arr[0]
            for i in arr[1:]:
                cs = max(i,cs+i)
                ms = max(cs,ms)
            return ms
        max_kadane = kadane(nums)
        totalsum = sum(nums)
        min_subarray = kadane([-x for x in nums])
        max_circular = totalsum+min_subarray
        return max(max_circular,max_kadane) if max_circular!=0 else max_kadane