class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        a = {}
        b = {}
        s = s.split(" ")
        if len(pattern)!=len(s):
            return False
        for i in range(len(s)):
            m,n = s[i],pattern[i]
            if (m in a and a[m]!=n) or (n in b and b[n]!=m):
                return False
            a[m]=n
            b[n] = m
        return True