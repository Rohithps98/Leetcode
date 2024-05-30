class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        neg = set()
        for i in nums:
            if i<0:
                neg.add(i)
        ans = -1
        for i in nums:
            if i>ans and -i in neg:
                ans = i
        return ans