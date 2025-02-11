from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l = len(p)
        res = []
        cp = Counter(p)
        sp = Counter(s[:l])
        for i in range(len(s)-l+1):
            if sp == cp:
                res.append(i)
            if i+l<len(s):
                sp[s[i]]-=1
                if sp[s[i]]==0:
                    del sp[s[i]]
                sp[s[i+l]]+=1
        return res