class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        a = {}
        for i in s:
            a[i] = a.get(i,0)+1
        for i in t:
            if i not in a or a[i]==0:
                return i
            a[i]-=1
        return ''