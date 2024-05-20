class Solution:
    def reverse(self, x: int) -> int:
        intmax = 2**31-1
        rev = 0
        sign = 1 if x>=0 else -1
        x = abs(x)
        while x!=0:
            pop = x%10
            x = x//10
            if rev>(intmax-pop)//10:
                return 0
            rev = rev*10+pop
        return rev*sign