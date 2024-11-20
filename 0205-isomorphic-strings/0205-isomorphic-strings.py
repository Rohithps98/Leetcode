class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        a,b = {},{}
        for i,j in zip(s,t):
            if i not in a and j not in b:
                a[i] = j
                b[j] = i
            elif a.get(i)!=j or b.get(j)!=i:
                return False
        return True