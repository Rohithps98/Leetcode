class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        a = collections.Counter(arr)
        b = list(a.values())
        c = set(b)
        return len(b)==len(c)