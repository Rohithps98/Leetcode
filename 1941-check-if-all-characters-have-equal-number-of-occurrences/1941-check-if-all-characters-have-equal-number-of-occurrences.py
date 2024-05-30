from collections import Counter
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        a = Counter(s)
        b = set()
        for i,j in a.items():
            if j not in b:
                b.add(j)
        return not len(b)>1