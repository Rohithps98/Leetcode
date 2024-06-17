class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        if indexDiff<1 or valueDiff<0:
            return False
        bucket={}
        width = valueDiff+1
        def get_bid(num):
            return num//width
        for i,num in enumerate(nums):
            bid = get_bid(num)
            if bid in bucket:
                return True
            if bid-1 in bucket and abs(num-bucket[bid-1])<width:
                return True
            if bid+1 in bucket and abs(num-bucket[bid+1])<width:
                return True
            bucket[bid]=num
            if i>=indexDiff:
                del bucket[get_bid(nums[i-indexDiff])]
        return False