class Solution:
    def scoreOfString(self, s: str) -> int:
        su = 0
        for i in range(len(s)-1):
            su+=abs(ord(s[i])-ord(s[i+1]))
        return su