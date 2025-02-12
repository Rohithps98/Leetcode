class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def digitsum(n):
            return sum(int(d) for d in str(n))
        dm = {}
        maxsum = -1
        for n in nums:
            ds = digitsum(n)
            if ds in dm:
                maxsum = max(maxsum,n+dm[ds])
                dm[ds] = max(dm[ds],n)
            else:
                dm[ds] = n
        return maxsum