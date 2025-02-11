from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l = len(p)
        res = []
        cp = Counter(p)
        cs = Counter(s[:l])
        for i in range(len(s)-l+1):
            if cp==cs:
                res.append(i)
            if i+l<len(s):
                cs[s[i]]-=1
                if cs[s[i]]==0:
                    del cs[s[i]]
                cs[s[i+l]]+=1
        return res

# class Solution:
#     def findAnagrams(self, s: str, p: str) -> List[int]:
#         l = len(p)
#         p = sorted(p)
#         res = []
#         i = 0
#         while i<len(s):
#             if i+l<=len(s):
#                 if s==p:
#                     res.append(i)
#                 elif sorted(s[i:i+l])==p:
#                     res.append(i)
#             i+=1
#         return res