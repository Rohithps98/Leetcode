class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left = 0
        count = 0
        charcount = {'a':0,'b':0,'c':0}
        n = len(s)
        for right in range(n):
            charcount[s[right]]+=1
            while charcount['a']>0 and charcount['b']>0 and charcount['c']>0:
                count+=n-right
                charcount[s[left]]-=1
                left+=1
        return count