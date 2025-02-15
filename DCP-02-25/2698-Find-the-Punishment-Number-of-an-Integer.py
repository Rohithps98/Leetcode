class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        total = 0
        left = 0
        right = len(nums)-1
        while left<=right:
            if left<right:
                num = int(str(nums[left])+str(nums[right]))
                total+=num
            else:
                total+=nums[left]
            print(total)
            left+=1
            right-=1
        return total