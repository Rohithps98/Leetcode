class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        ma,mi = 1,1
        for n in nums:
            if n==0:
                ma,mi = 1,1
                continue
            tmp = ma*n
            ma = max(n,tmp,mi*n)
            mi = min(n,tmp,mi*n)
            res = max(ma,res)
        return res