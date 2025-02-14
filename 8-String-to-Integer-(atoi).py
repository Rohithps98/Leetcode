class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0
        i = 0
        sign = 1
        if s[i] in ['-','+']:
            if s[i]=='-':
                sign = -1
            i+=1
        mi = -2**31
        ma = 2**31-1
        res = 0
        while i<len(s) and s[i].isdigit():
            digit = int(s[i])
            if res>(ma-digit)//10:
                return ma if sign==1 else mi
            res = res*10+digit
            i+=1
        return res*sign