class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            a = bin(i)[2:].count('1')
            res.append(a)
        return res