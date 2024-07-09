class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cumsum = 0
        sf = {0:1}
        count = 0
        for i in nums:
            cumsum+=i
            if cumsum-k in sf:
                count+=sf[cumsum-k]
            if cumsum in sf:
                sf[cumsum]+=1
            else:
                sf[cumsum]=1
        return count