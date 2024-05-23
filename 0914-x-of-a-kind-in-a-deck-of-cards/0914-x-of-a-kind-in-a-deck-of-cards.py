from collections import Counter
from math import gcd
from functools import reduce
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck)<2:
            return False
        a = Counter(deck)
        vals = list(a.values())
        def findgcd(lis):
            x = lis[0]
            for i in lis[1:]:
                x = gcd(x,i)
            return x
        return findgcd(vals)>1