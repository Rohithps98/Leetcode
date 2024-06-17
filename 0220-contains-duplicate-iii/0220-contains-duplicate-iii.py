class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        if indexDiff<1 or valueDiff<0:
            return False
        bucket = {}
        width = valueDiff+1
        def getbid(num):
            return num//width
        for i,num in enumerate(nums):
            bid = getbid(num)
            if bid in bucket:
                return True
            if bid-1 in bucket and abs(num-bucket[bid-1])<width:
                return True
            if bid+1 in bucket and abs(num-bucket[bid+1])<width:
                return True
            bucket[bid]=num
            if i>=indexDiff:
                del bucket[getbid(nums[i-indexDiff])]
        return False