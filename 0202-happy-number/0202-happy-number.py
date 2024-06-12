class Solution:
    def isHappy(self, n: int) -> bool:
        def nex(n):
            return sum(int(x)**2 for x in str(n))
        slow = n
        fast = nex(n)
        while fast!=1 and slow!=fast:
            slow=nex(slow)
            fast = nex(nex(fast))
        return fast==1