class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        a = []
        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)-2):
                lo = j+1
                hi = len(nums)-1
                while lo<hi:
                    # cu = nums[i]+nums[j]+nums[left]+nums[right]
                    if nums[lo]+nums[hi]+nums[i]+nums[j] == target and sorted([nums[i],nums[j],nums[lo],nums[hi]]) not in a:
                        a.append([nums[i],nums[j],nums[lo],nums[hi]])
                        lo+=1
                        hi-=1
                    elif nums[lo]+nums[hi]+nums[i]+nums[j] > target:
                        hi-=1
                    else:
                        lo+=1

        return a