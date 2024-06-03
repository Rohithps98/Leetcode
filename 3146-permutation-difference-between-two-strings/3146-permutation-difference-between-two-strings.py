class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        a,b = {},{}
        for i,j in enumerate(s):
            a[j] = i
        for i,j in enumerate(t):
            b[j]= i
        su = 0
        for i,j in a.items():
            if i in b:
                su+=abs(a[i]-b[i])
        return su