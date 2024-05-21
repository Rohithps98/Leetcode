class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        while n and n not in visit:
            visit.add(n)
            n = self.ssq(n)
            if n==1:
                return True
        return False
    def ssq(self,n):
        res = 0
        while n:
            d = n%10
            d = d**2
            res+=d
            n//=10
        return res