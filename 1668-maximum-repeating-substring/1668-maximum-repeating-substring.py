class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        a = len(word)
        i = 0
        k = 0
        while word*(k+1) in sequence:
            k+=1
        # while i<len(sequence):
        #     if sequence[i:i+a]==word:
        #         k+=1
        #         i = i+a
        #     else:
        #         i+=1
        return k