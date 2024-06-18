class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = {}
        for i in strs:
            b = ''.join(sorted(i))
            if b not in a:
                a[b] = [i]
            else:
                a[b].append(i)
        return a.values()