class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,mp = 0,0
        for r in range(len(prices)):
            pr = prices[r]-prices[l]
            if pr>0:
                mp = max(mp,pr)
            else:
                l = r
        return mp