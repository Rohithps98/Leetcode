class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        # k = 0
        # while (k+1)*word in sequence:
        #     k+=1
        # return k
        n,m = len(sequence),len(word)
        dp = [0]*n
        k = 0
        for i in range(n):
            if i>=m-1 and sequence[i-m+1:i+1]==word:
                dp[i]=dp[i-m]+1 if i>=m else 1
            else:
                dp[i] = 0
            k = max(k,dp[i])
        return k