class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i,a in enumerate(nums):
            if i>0 and nums[i-1]==a:
                continue
            l,r = i+1,len(nums)-1
            while l<r:
                su = a+nums[l]+nums[r]
                if su>0:
                    r-=1
                elif su<0:
                    l+=1
                else:
                    res.append([a,nums[l],nums[r]])
                    l+=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
        return res