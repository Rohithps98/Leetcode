class Solution:
    def climbStairs(self, n: int) -> int:
        one = 2
        two = 1
        if n==1 or n==2:
            return n
        for i in range(3,n+1):
            cur = one+two
            two = one
            one = cur
        return one