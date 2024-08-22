class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pre = {}
        for i,num in enumerate(nums):
            if target-num in pre:
                return [i,pre[target-num]]
            pre[num] = i