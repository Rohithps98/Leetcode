import heapq
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        count = 0
        while nums[0]<k:
            if len(nums)<2:
                return -1
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            heapq.heappush(nums,x*2+y)
            count+=1
        return count
        # nums.sort(reverse = True)
        # count = 0
        # while min(nums)<k:
        #     x = nums.pop()
        #     y = nums.pop()
        #     nums.append(x*2+y)
        #     nums.sort(reverse = True)
        #     count+=1
        # return count