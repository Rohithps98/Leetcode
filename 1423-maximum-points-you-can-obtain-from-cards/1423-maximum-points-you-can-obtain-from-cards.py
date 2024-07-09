class Solution:
    def maxScore(self, cardpoints: List[int], k: int) -> int:
        n = len(cardpoints)
        windowsize = n-k
        currentsum = sum(cardpoints[:windowsize])
        minsum = currentsum
        for i in range(windowsize,n):
            currentsum+=cardpoints[i]-cardpoints[i-windowsize]
            minsum = min(minsum,currentsum)
        totalsum = sum(cardpoints)
        return totalsum-minsum