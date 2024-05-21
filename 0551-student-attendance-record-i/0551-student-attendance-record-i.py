class Solution:
    def checkRecord(self, s: str) -> bool:
        a = collections.Counter(s)
        if a['A']>=2 or 'LLL' in s:
            return False
        return True