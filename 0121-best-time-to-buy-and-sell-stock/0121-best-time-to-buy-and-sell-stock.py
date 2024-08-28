class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,mp = 0,0
        for r in range(len(prices)):
            pro = prices[r]-prices[l]
            if pro>0:
                mp = max(mp,pro)
            else:
                l = r
        return mp