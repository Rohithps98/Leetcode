class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        a = {}
        su = 0
        for i,j in enumerate(s):
            a[j] = i
        for i in range(len(t)):
            su+=abs(i-a[t[i]])
        return su