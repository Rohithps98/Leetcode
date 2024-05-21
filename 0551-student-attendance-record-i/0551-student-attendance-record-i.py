class Solution:
    def checkRecord(self, s: str) -> bool:
        a = collections.Counter(s)
        if 'A' in a and a['A']>=2:
            return False
        for i in range(len(s)-2):
            if s[i]=='L':
                if s[i+1]==s[i+2]=='L':
                    return False
        return True