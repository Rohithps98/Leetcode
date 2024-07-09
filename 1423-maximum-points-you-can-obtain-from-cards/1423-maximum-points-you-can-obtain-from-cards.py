class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        windowsize = n-k
        currentsum = sum(cardPoints[:windowsize])
        minsum = currentsum
        for i in range(windowsize,n):
            currentsum+=cardPoints[i]-cardPoints[i-windowsize]
            minsum = min(minsum,currentsum)
        totalsum = sum(cardPoints)
        return totalsum-minsum