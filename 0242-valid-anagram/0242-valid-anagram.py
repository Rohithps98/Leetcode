class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a,b = {},{}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            a[s[i]] = 1+a.get(s[i],0)
            b[t[i]] = 1+b.get(t[i],0)
        return a==b