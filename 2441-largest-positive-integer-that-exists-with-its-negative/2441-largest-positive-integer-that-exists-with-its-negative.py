class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        l,r = 0,len(nums)-1
        while l<r:
            if -nums[l]==nums[r]:
                return nums[r]
            elif -nums[l]>nums[r]:
                l+=1
            else:
                r-=1
        return -1
        # neg = set()
        # for i in nums:
        #     if i<0:
        #         neg.add(i)
        # ans = -1
        # for i in nums:
        #     if i>ans and -i in neg:
        #         ans = i
        # return ans