class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=='':
            return ''
        countt,window = {},{}
        for i in t:
            countt[i] = 1+countt.get(i,0)
        l,have,need = 0,0,len(countt)
        res,resl = [-1,-1],float('inf')
        for r in range(len(s)):
            c = s[r]
            window[c] = 1+window.get(c,0)
            if c in countt and countt[c] == window[c]:
                have+=1
            while have==need:
                if resl>r-l+1:
                    res = [l,r]
                    resl = r-l+1
                window[s[l]]-=1
                if s[l] in countt and window[s[l]]<countt[s[l]]:
                    have-=1
                l+=1
        l,r = res
        return s[l:r+1] if resl!=float('inf') else ''