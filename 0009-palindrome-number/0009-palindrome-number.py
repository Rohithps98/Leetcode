class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        if x%10==0 and x!=0:
            return False
        a = 0
        while x>a:
            a = (a*10)+(x%10)
            x//=10
        return x==a or x==a//10