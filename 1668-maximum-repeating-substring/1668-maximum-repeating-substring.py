class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        k = 0
        while (k+1)*word in sequence:
            k+=1
        return k