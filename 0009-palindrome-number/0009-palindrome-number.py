class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        if x>=0 and x<10:
            return True
        a = 0
        c = x
        while x:
            n = x%10
            a = (a*10)+n
            x = x//10
            print(x)
        print(a)
        return a==c