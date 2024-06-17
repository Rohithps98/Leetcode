class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        if indexDiff<1 or valueDiff<0:
            return False
        bucket = {}
        width = valueDiff+1
        def get_bucketid(num):
            return num//width
        for i,num in enumerate(nums):
            bucket_id = get_bucketid(num)
            if bucket_id in bucket:
                return True
            if bucket_id-1 in bucket and abs(num-bucket[bucket_id-1])<width:
                return True
            if bucket_id+1 in bucket and abs(num-bucket[bucket_id+1])<width:
                return True
            bucket[bucket_id] = num
            if i>=indexDiff:
                del bucket[get_bucketid(nums[i-indexDiff])]
        return False