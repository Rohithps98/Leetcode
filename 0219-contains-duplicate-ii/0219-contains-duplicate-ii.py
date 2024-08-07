class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        a = {}
        for i,j in enumerate(nums):
            if j in a and abs(i-a[j])<=k:
                return True
            a[j] = i
        return False