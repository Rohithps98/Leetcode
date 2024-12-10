class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        if n==0:
            return []
        result = [words[0]]
        last = groups[0]
        for i in range(1,len(groups)):
            if groups[i]!=last:
                result.append(words[i])
                last = groups[i]
        return result