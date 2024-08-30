class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def gp(s,l,r):
            if len(s)==2*n:
                res.append(s)
                return
            if l<n:
                gp(s+'(',l+1,r)
            if r<l:
                gp(s+')',l,r+1)
        gp('',0,0)
        return res