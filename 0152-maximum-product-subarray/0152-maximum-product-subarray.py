class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        mi,ma = 1,1
        for i in nums:
            if i==0:
                ma,mi = 1,1
            tmp = ma*i
            ma = max(i,tmp,mi*i)
            mi = min(i,tmp,mi*i)
            res = max(ma,res)
        return res