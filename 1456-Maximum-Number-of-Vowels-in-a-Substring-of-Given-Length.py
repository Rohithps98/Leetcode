class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        v = {'a','e','i','o','u'}
        maxcount = 0
        curr = sum(1 for i in range(k) if s[i] in v)
        maxcount = curr
        for i in range(k,len(s)):
            if s[i] in v:
                curr+=1
            if s[i-k] in v:
                curr-=1
            maxcount = max(maxcount,curr)
        return maxcount