class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        a = 0
        c = x
        while x:
            n = x%10
            a = (a*10)+n
            x = x//10
        return a==c