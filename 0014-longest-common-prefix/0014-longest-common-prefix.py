class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        a = float('inf')
        for i in strs:
            if len(i)<a:
                a = len(i)
        i= 0
        while i<a:
            for j in strs:
                if j[i]!=strs[0][i]:
                    return j[:i]
            i+=1
        return strs[0][:i]