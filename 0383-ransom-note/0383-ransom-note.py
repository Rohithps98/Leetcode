class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a = Counter(ransomNote)
        b = Counter(magazine)
        for c in a:
            if c not in b or a[c]>b[c]:
                return False
        return True